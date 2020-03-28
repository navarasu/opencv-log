import cvlog as log
import cv2
from bs4 import BeautifulSoup
from .utils import read_file,remove_dirs
import os
from unittest.mock import patch

def test_default_mode_default_level():
    remove_dirs('log/')
    log_all_level(cv2.imread("tests/data/orange.png"))
    assert os.path.exists('log/log.html') == False

def test_log_mode_default_level():
    remove_dirs('log/')
    log.set_mode(log.Mode.LOG)
    log_all_level(cv2.imread("tests/data/orange.png"))
    logitem = get_html('log/log.html').select('.log-list .log-item')
    assert len(logitem) == 1
    level_tag = logitem[0].select('.level')[0]
    assert level_tag.get_text() == 'ERROR'
    assert level_tag['class'] == ['level', 'error']

@patch('cvlog.log.show_image')
def test_debug_mode_default_level(show_image):
    remove_dirs('log/')
    log.set_mode(log.Mode.DEBUG)
    show_image.return_value=ord("y")
    log_all_level(cv2.imread("tests/data/orange.png"))
    assert os.path.exists('log/log.html') == False

def log_all_level(img):
    log.image(log.Level.TRACE, img)
    log.image(log.Level.INFO, img)
    log.image(log.Level.ERROR, img)

def get_html(file):
    return BeautifulSoup(read_file(file), 'html.parser')