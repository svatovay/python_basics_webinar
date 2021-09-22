import os
import yaml

with open('config.yaml', 'r') as f:
    starter = yaml.safe_load(f)

def create_path(values, prefix=""):
    for direcory, path in values.items():
        dir_path = os.path.join(prefix, direcory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(path, dict):
            create_path(path, dir_path)
        else:
            for i in path:
                if isinstance(i, dict):
                    create_path(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass
create_path(starter)
