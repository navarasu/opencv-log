import os
from shutil import rmtree
ROOT_DIR = os.path.abspath(os.curdir)

def read_file(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
    return content

def remove_dirs(dir_path):
    if os.path.exists(dir_path):
        rmtree(dir_path)
