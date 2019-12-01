

def read_file(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
    return content