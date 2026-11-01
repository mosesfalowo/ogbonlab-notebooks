# Render assets/fd-lab-wavefield.gif: the ssm_acoustic_fd_lab notebook's
# own arrays, animated as its time loop runs. Same model, same stencil, same
# sponge, same source: the notebook's field_shot() runs its own run(), and this
# script only hands it a list to keep the wavefield in (frame capture is the
# one addition). Run from the repo root:
#   python3 tools/render_fd_gif.py          (or give the root: python3 render_fd_gif.py <root>)
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB = os.path.join(ROOT, 'notebooks', 'ssm_acoustic_fd_lab.ipynb')
OUT = os.path.join(ROOT, 'assets', 'fd-lab-wavefield.gif')
EVERY_MS = 14.0     # one frame every 14 ms of the run

# The notebook's code, defined but not run (its main() waits for __main__):
# every function and constant below is the notebook's own.
nb = json.load(open(NB))
code = '\n\n'.join(''.join(c['source'])
                   for c in nb['cells'] if c['cell_type'] == 'code')
ns = {'__name__': 'render_fd_gif'}
exec(compile(code, NB, 'exec'), ns)

frames = []
s = ns['field_shot'](ns['WINDOW'], ns['F_PEAK_HZ'], frames, EVERY_MS)
v, h, dt, nt, N_ABS = s['v'], s['h'], s['dt'], s['nt'], ns['N_ABS']
every = max(1, int(EVERY_MS * 1e-3 / dt))           # as field_shot counts it
xk = (s['x0'] + np.arange(v.shape[1]) * h) / 1e3
zm = np.arange(v.shape[0]) * h
t_ms = np.arange(nt) * dt * 1000.0
mute = t_ms[:, None] > 1e6 * np.abs(xk - xk[xk.size // 2])[None, :] / ns['MUTE_MPS'] + ns['MUTE_MS']
diff = (s['rec'] - s['bg']) * mute * (t_ms[:, None] / 1000.0) ** 2   # as the notebook's figure shows it
inner = [u[N_ABS:N_ABS + v.shape[0], N_ABS:N_ABS + v.shape[1]] for u in frames]

peak_r = np.abs(diff).max() * ns['CLIP'] + 1e-30
T_REF_MS = 150.0    # the wavefield clip: its peak at 150 ms, falling as one over the square root of time after it
peak_u = np.abs(inner[int(T_REF_MS / (every * dt * 1000.0))]).max() * 0.6 + 1e-30

fig, ax = plt.subplots(1, 2, figsize=(10.4, 4.4), dpi=80, gridspec_kw={'width_ratios': [1.2, 1]})
ax[0].imshow(v / 1e3, cmap='bone', aspect='auto', extent=[xk[0], xk[-1], zm[-1], 0])
im_u = ax[0].imshow(np.zeros_like(v), cmap='seismic', vmin=-1.0, vmax=1.0, alpha=0.6,
                    aspect='auto', extent=[xk[0], xk[-1], zm[-1], 0])
ax[0].set_title('the wavefield in the field earth, clip falling as one over root time', fontsize=10)
ax[0].set_xlabel('distance (km)'); ax[0].set_ylabel('depth (m)')
stamp = ax[0].text(0.02, 0.96, '', transform=ax[0].transAxes, fontsize=9, va='top',
                   bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
im_r = ax[1].imshow(np.zeros_like(diff), cmap='gray_r', vmin=-peak_r, vmax=peak_r, aspect='auto',
                    extent=[xk[0], xk[-1], t_ms[-1], 0])
ax[1].set_title('what the structure adds to the record', fontsize=10)
ax[1].set_xlabel('receiver position (km)'); ax[1].set_ylabel('time (ms), gain t squared')
plt.tight_layout()

def draw(i):
    it = i * every
    im_u.set_data(inner[i] / (peak_u * np.sqrt(T_REF_MS / max(t_ms[min(it, nt - 1)], T_REF_MS))))
    shown = diff.copy(); shown[it + 1:] = 0.0
    im_r.set_data(shown)
    stamp.set_text('%.0f ms' % t_ms[min(it, nt - 1)])
    return im_u, im_r, stamp

anim = FuncAnimation(fig, draw, frames=len(inner), interval=70)
anim.save(OUT, writer=PillowWriter(fps=14))

# palette-optimize in place; identical frames, smaller file
from PIL import Image, ImageSequence
im = Image.open(OUT)
seq = [f.convert('P', palette=Image.ADAPTIVE, colors=128)
       for f in ImageSequence.Iterator(im)]
seq[0].save(OUT, save_all=True, append_images=seq[1:],
            duration=im.info.get('duration', 70), loop=0, optimize=True)
print('wrote', os.path.relpath(OUT, ROOT), '%d frames, %.1f KB' % (len(seq), os.path.getsize(OUT) / 1024.0))
