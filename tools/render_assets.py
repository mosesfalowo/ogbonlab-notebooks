# Render the README assets by RUNNING each notebook's code cells, so every
# figure in assets/ is the unedited output of its notebook. Run from the
# repo root:  python3 tools/render_assets.py   (or give the root: python3 render_assets.py <root>)
# Each notebook runs as Colab runs it, under __name__ == '__main__', and its
# wall time is printed.
import json
import glob
import os
import sys
import tempfile
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, 'assets')

# notebooks whose figures the README shows; the FD lab ships as a GIF
# rendered by tools/render_fd_gif.py, and its still figure too
SKIP = set()

# the flagship produces two figures; name them explicitly
MULTI = {'ssm_field_realistic_section': ['ssm_field_realistic_section_geology',
                                         'ssm_field_realistic_section']}

os.makedirs(ASSETS, exist_ok=True)
work = tempfile.mkdtemp(prefix='ogbon-assets-')
os.chdir(work)   # notebook side files (the ML .npz) land here, not in git

total = 0.0
for path in sorted(glob.glob(os.path.join(ROOT, 'notebooks', '*.ipynb'))):
    base = os.path.splitext(os.path.basename(path))[0]
    if base in SKIP:
        continue
    nb = json.load(open(path))
    code = '\n\n'.join(''.join(c['source'])
                       for c in nb['cells'] if c['cell_type'] == 'code')
    plt.close('all')
    t0 = time.time()
    exec(compile(code, path, 'exec'), {'__name__': '__main__'})   # as Colab runs it
    dt = time.time() - t0
    total += dt
    figs = [plt.figure(n) for n in plt.get_fignums()]
    names = MULTI.get(base, [base])
    if len(figs) < len(names):
        raise SystemExit('%s: expected %d figures, got %d'
                         % (base, len(names), len(figs)))
    for fig, name in zip(figs[-len(names):], names):
        out = os.path.join(ASSETS, name + '.png')
        fig.savefig(out, dpi=120, bbox_inches='tight')
        print('wrote', os.path.relpath(out, ROOT))
    print('ran %s in %.2f s' % (base, dt))
print('assets rendered; the notebooks ran in %.2f s together' % total)
