from cvlog.html_logger import HtmlLogger
import pytest
import re
report_path="log"

def test_init_html_logger():
    log=HtmlLogger(report_path+'/init.html')
    assert read_file(report_path+'/init.html') == read_file('data/expected/init.html') 

def read_file(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
    return re.sub(r"[\n]*", "", content)
    