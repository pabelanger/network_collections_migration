import os


for dirpath, dirname, filenames in os.walk('.'):
    for f in filenames:
        if '__init__.py' in f or not f.startswith('_'):
            continue
        src = os.path.join(dirpath, f)
        dest = os.path.join(dirpath, f[1:])
        os.rename(src, dest)
