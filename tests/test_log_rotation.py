import cvlog as log
import cv2
from .utils import remove_dirs
import os
import cvlog.html_logger as hl
import time

def test_log_interruption():
    remove_dirs('log/')
    log.set_mode(log.Mode.LOG)
    img = cv2.imread("tests/data/orange.png")
    log.error.image(img)
    assert os.path.exists('log/cvlog.html') is True
    remove_dirs('log/')
    log.error.image(img)
    assert os.path.exists('log/cvlog.html') is True

def test_log_path():
    log.set_mode(log.Mode.LOG)
    log.set_path("check/")
    img = cv2.imread("tests/data/orange.png")
    log.error.image(img)
    assert os.path.exists('check/cvlog.html') is True
    log.set_path("log/")

def test_log_rotation():
    remove_dirs('log/')
    html_logger = hl.HtmlLogger()
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    assert os.path.exists('check/cvlog.html') is True
    assert len(os.listdir('log/')) == 1
    html_logger = hl.HtmlLogger()
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    time.sleep(1)
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    assert os.path.exists('check/cvlog.html') is True
    assert len(os.listdir('log/')) == 2
    html_logger = hl.HtmlLogger()
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    assert os.path.exists('check/cvlog.html') is True
    assert len(os.listdir('log/')) == 3
    html_logger = hl.HtmlLogger()
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    html_logger.log_image('error', 'LoggerName', 'image', "dummy string", None)
    assert os.path.exists('check/cvlog.html') is True
    assert len(os.listdir('log/')) == 4
