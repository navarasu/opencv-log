import cvlog as log
import cv2
from .utils import remove_dirs
import os

def test_log_interruption():
    remove_dirs('log/')
    log.set_mode(log.Mode.LOG)
    img = cv2.imread("tests/data/orange.png")
    log.image(log.Level.ERROR, img)
    assert os.path.exists('log/cvlog.html') is True
    remove_dirs('log/')
    log.image(log.Level.ERROR, img)
    assert os.path.exists('log/cvlog.html') is True

def test_log_path():
    log.set_mode(log.Mode.LOG)
    log.set_path("check/")
    img = cv2.imread("tests/data/orange.png")
    log.image(log.Level.ERROR, img)
    assert os.path.exists('check/cvlog.html') is True
    log.set_path("log/")
