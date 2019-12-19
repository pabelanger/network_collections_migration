import os
from ruamel.yaml import YAML


def read_yaml_file(filename):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True

    data = None
    with open(filename, 'r') as stream:
        data = yaml.load(stream)

    with open(filename, 'w') as f:
        yaml.dump(data, f)


def read_meta_file(filename):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.indent(sequence=4, offset=2)

    data = None
    with open(filename, 'r') as stream:
        data = yaml.load(stream)

    with open(filename, 'w') as f:
        yaml.dump(data, f)


files = []
meta_files = []

for dirpath, dirname, filenames in os.walk('.'):
    for f in filenames:
        if '.yml' in f or '.yaml' in f:
            if 'meta' in dirpath:
                meta_files.append(os.path.join(dirpath, f))
                continue

            files.append(os.path.join(dirpath, f))

for f in files:
    read_yaml_file(f)

for f in meta_files:
    read_meta_file(f)
