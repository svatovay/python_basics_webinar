import os
import shutil

starter = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
root_dir = starter.pop(0)
for dir in starter:
    dir_path = os.path.join(root_dir, dir)
    os.makedirs(dir_path)

# shutil.rmtree('my_project')
