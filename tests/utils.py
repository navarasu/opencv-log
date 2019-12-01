import os
from shutil import rmtree
def read_file(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
    return content

def remove_dirs(dir_path):
    if os.path.exists(dir_path):
        rmtree('log/report')