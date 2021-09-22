import os
import shutil


def scan(item):
    for item in os.scandir(os.path.abspath(item)):
        if os.path.isdir(os.path.abspath(item)):
            scan(item)
        elif os.path.isfile(os.path.abspath(item)) and str(item).split('.')[1][:4] == 'html':
            src = os.path.split(os.path.dirname(os.path.abspath(item)))[0]
            dst = os.path.join(os.path.abspath(r'my_project\templates'),
                               os.path.split(os.path.dirname(os.path.abspath(item)))[1])
            # print(src)
            # print(dst)
            shutil.copytree(src,
                            dst,
                            symlinks=False,
                            ignore=None,
                            copy_function=shutil.copy2,
                            ignore_dangling_symlinks=False)


scan('my_project')
