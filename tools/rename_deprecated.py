import os


for dirpath, dirname, filenames in os.walk('.'):
    for f in filenames:
        if '__init__.py' in f or not f.startswith('_'):
            continue
        # NOTE(pabelanger): _net_* renames
        if '_net_' not in f:
          continue
        src = os.path.join(dirpath, f)
        dest = os.path.join(dirpath, f[1:])
        print('Renaming %s -> %s', src, dest)
        os.rename(src, dest)
