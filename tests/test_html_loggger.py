from cvlog.html_logger import HtmlLogger
import pytest
import re
report_path=".report"

def test_init_html_logger():
    log=HtmlLogger(report_path+'/init.html')
    assert read_file(report_path+'/init.html') == "<html><body></body></html>"

def test_log_image():
    log=HtmlLogger(report_path+'/image.html')
    log.log_image('text')
    assert read_file(report_path+'/image.html') == '<html><body><img src="data:image/png;base64, text"/></body></html>'

def read_file(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
    return re.sub(r"[\n]*", "", content)
    