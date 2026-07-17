# Render assets/fd-lab-wavefield.gif: the ssm_acoustic_fd_lab notebook's
# arrays, animated as its time loop runs. Same physics, same model, same
# solver; this script only adds frame capture. Run from the repo root:
#   python3 tools/render_fd_gif.py
import json
import os

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB = os.path.join(ROOT, 'notebooks', 'ssm_acoustic_fd_lab.ipynb')
OUT = os.path.join(ROOT, 'assets', 'fd-lab-wavefield.gif')

# Pull the notebook's own code and cut it just before its time loop, so the
# model, grid, sponges, and source below are literally the notebook's.
nb = json.load(open(NB))
code = '\n\n'.join(''.join(c['source'])
                   for c in nb['cells'] if c['cell_type'] == 'code')
head = code[:code.index('for it in range(NT):')]
ns = {}
exec(compile(head, NB, 'exec'), ns)

N, NT, DT, H = ns['N'], ns['NT'], ns['DT'], ns['H']
c2, damp, src = ns['c2'], ns['damp'], ns['src']
v, F_MAX, SX, SZ = ns['v'], ns['F_MAX'], ns['SX'], ns['SZ']
u0 = np.zeros((N, N)); u1 = np.zeros((N, N))
record = np.zeros((NT, N))

# dense frames while the wavefield is alive, sparse after, so the GIF
# spends its time on propagation and still lets the record finish
capture_at = set(np.linspace(0, int(NT * 0.55), 48).astype(int)) \
    | set(np.linspace(int(NT * 0.55), NT - 1, 14).astype(int))
frames = []
for it in range(NT):
    lap = (np.roll(u1, 1, 0) + np.roll(u1, -1, 0) +
           np.roll(u1, 1, 1) + np.roll(u1, -1, 1) - 4 * u1)
    u2 = 2 * u1 - u0 + c2 * lap
    u2[SZ, SX] += src(it, F_MAX * 0.6) * DT ** 2 * 1e6
    u2[0, :] = 0
    u1 = u1 * damp; u2 = u2 * damp
    record[it] = u2[2, :]
    if it in capture_at:
        frames.append((it, u2.copy(), record.copy()))
    u0, u1 = u1, u2

peak_u = max(np.percentile(np.abs(f[1]), 99.5) for f in frames[8:]) + 1e-12
peak_r = np.percentile(np.abs(record), 99.0) * 1.2 + 1e-12

fig, ax = plt.subplots(1, 2, figsize=(9.6, 4.3), dpi=80)
im_v = ax[0].imshow(v, cmap='bone', vmin=v.min() - 0.35 * (v.max() - v.min()))
im_u = ax[0].imshow(np.zeros((N, N)), cmap='seismic',
                    vmin=-peak_u, vmax=peak_u, alpha=0.62)
ax[0].set_title('wavefield snapshot')
ax[0].set_axis_off()
im_r = ax[1].imshow(np.zeros((NT, N)), cmap='gray',
                    vmin=-peak_r, vmax=peak_r, aspect='auto')
ax[1].set_title('surface record: diffractions live here')
ax[1].set_axis_off()
plt.tight_layout()

def draw(i):
    it, u, rec = frames[i]
    im_u.set_data(u)
    rec_masked = rec.copy(); rec_masked[it + 1:] = 0.0
    im_r.set_data(rec_masked)
    return im_u, im_r

anim = FuncAnimation(fig, draw, frames=len(frames), interval=70)
anim.save(OUT, writer=PillowWriter(fps=14))

# palette-optimize in place; identical frames, smaller file
from PIL import Image, ImageSequence
im = Image.open(OUT)
seq = [f.convert('P', palette=Image.ADAPTIVE, colors=128)
       for f in ImageSequence.Iterator(im)]
seq[0].save(OUT, save_all=True, append_images=seq[1:],
            duration=im.info.get('duration', 70), loop=0, optimize=True)
print('wrote', os.path.relpath(OUT, ROOT),
      '%.1f KB' % (os.path.getsize(OUT) / 1024.0))
