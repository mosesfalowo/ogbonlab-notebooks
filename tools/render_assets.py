# Render the README assets by RUNNING each notebook's code cells, so every
# figure in assets/ is the unedited output of its notebook. Run from the
# repo root:  python3 tools/render_assets.py
import json
import glob
import os
import tempfile

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, 'assets')

# notebooks whose figures the README shows; the FD lab ships as a GIF
# rendered by tools/render_fd_gif.py instead
SKIP = {'ssm_acoustic_fd_lab'}

# the flagship produces two figures; name them explicitly
MULTI = {'ssm_field_realistic_section': ['ssm_field_realistic_section_geology',
                                         'ssm_field_realistic_section']}

os.makedirs(ASSETS, exist_ok=True)
work = tempfile.mkdtemp(prefix='ogbon-assets-')
os.chdir(work)   # notebook side files (the ML .npz) land here, not in git

for path in sorted(glob.glob(os.path.join(ROOT, 'notebooks', '*.ipynb'))):
    base = os.path.splitext(os.path.basename(path))[0]
    if base in SKIP:
        continue
    nb = json.load(open(path))
    code = '\n\n'.join(''.join(c['source'])
                       for c in nb['cells'] if c['cell_type'] == 'code')
    plt.close('all')
    exec(compile(code, path, 'exec'), {})
    figs = [plt.figure(n) for n in plt.get_fignums()]
    names = MULTI.get(base, [base])
    if len(figs) < len(names):
        raise SystemExit('%s: expected %d figures, got %d'
                         % (base, len(names), len(figs)))
    for fig, name in zip(figs[-len(names):], names):
        out = os.path.join(ASSETS, name + '.png')
        fig.savefig(out, dpi=120, bbox_inches='tight')
        print('wrote', os.path.relpath(out, ROOT))
print('assets rendered')
