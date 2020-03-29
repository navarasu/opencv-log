from cvlog.html_logger import HtmlLogger
import pytest
from .utils import read_file
report_path="log"

def test_init_html_logger():
    HtmlLogger(report_path+'/html/init.html')
    assert read_file(report_path+'/html/init.html') == read_file('tests/data/expected/init.html')