import cvlog as log
import cv2
from .utils import remove_dirs
import os

def test_log_interruption():
    remove_dirs('log/')
    log.set_mode(log.Mode.LOG)
    img = cv2.imread("tests/data/orange.png")
    log.image(log.Level.ERROR, img)
    assert os.path.exists('log/log.html') is True
    remove_dirs('log/')
    log.image(log.Level.ERROR, img)
    assert os.path.exists('log/log.html') is True
