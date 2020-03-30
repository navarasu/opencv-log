import cvlog as log
import cv2
import numpy as np
from .utils import read_file, remove_dirs, get_html
import os
from unittest.mock import patch

def test_default_mode_default_level():
    remove_dirs('log/')
    log_all_level(cv2.imread("tests/data/orange.png"))
    assert os.path.exists('log/log.html') is False

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
    show_image.return_value = ord("y")
    log_all_level(cv2.imread("tests/data/orange.png"))
    assert os.path.exists('log/log.html') is False

def test_log_mode_info_level():
    remove_dirs('log/')
    log.set_mode(log.Mode.LOG)
    log.set_level(log.Level.INFO)
    log_all_level(cv2.imread("tests/data/orange.png"))
    logitem = get_html('log/log.html').select('.log-list .log-item')
    assert len(logitem) == 2
    level_info_tag = logitem[0].select('.level')[0]
    assert level_info_tag.get_text() == 'INFO'
    assert level_info_tag['class'] == ['level', 'info']
    level_error_tag = logitem[1].select('.level')[0]
    assert level_error_tag.get_text() == 'ERROR'
    assert level_error_tag['class'] == ['level', 'error']

@patch('cvlog.log.show_image')
def test_debug_mode_info_level(show_image):
    remove_dirs('log/')
    log.set_mode(log.Mode.DEBUG)
    log.set_level(log.Level.INFO)
    show_image.return_value = ord("y")
    log_all_level(cv2.imread("tests/data/orange.png"))
    assert os.path.exists('log/log.html') is False

def test_log_mode_trace_level():
    remove_dirs('log/')
    log.set_mode(log.Mode.LOG)
    log.set_level(log.Level.TRACE)
    log_all_level(cv2.imread("tests/data/orange.png"))
    logitem = get_html('log/log.html').select('.log-list .log-item')
    assert len(logitem) == 3
    level_trace_tag = logitem[0].select('.level')[0]
    assert level_trace_tag.get_text() == 'TRACE'
    assert level_trace_tag['class'] == ['level', 'trace']
    level_info_tag = logitem[1].select('.level')[0]
    assert level_info_tag.get_text() == 'INFO'
    assert level_info_tag['class'] == ['level', 'info']
    level_error_tag = logitem[2].select('.level')[0]
    assert level_error_tag.get_text() == 'ERROR'
    assert level_error_tag['class'] == ['level', 'error']

@patch('cvlog.log.show_image')
def test_debug_mode_trace_level(show_image):
    remove_dirs('log/')
    log.set_mode(log.Mode.DEBUG)
    log.set_level(log.Level.TRACE)
    show_image.return_value = ord("y")
    log_all_level(cv2.imread("tests/data/orange.png"))
    assert os.path.exists('log/log.html') is False

def test_log_hough_lines():
    remove_dirs('log/')
    img = cv2.imread('tests/data/sudoku.png')
    log.set_mode(log.Mode.LOG)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    log.hough_lines(log.Level.ERROR, lines, img)
    logitem = get_html('log/log.html').select('.log-list .log-item')
    assert logitem[0]['logdata'] == read_file('tests/data/expected/houghline_img.txt')

def log_all_level(img):
    log.image(log.Level.TRACE, img)
    log.image(log.Level.INFO, img)
    log.image(log.Level.ERROR, img)
