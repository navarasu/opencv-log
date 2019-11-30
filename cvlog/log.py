import cv2
import os
import cvlog.html_logger as hl
import base64
from cvlog.config import Config,Mode,Level
html_logger= None

def image(level,image):
    if image is None:
        return
    try:
        __init()
        if Config().curent_level().value < level.value:
            return
        if Config().curent_mode() == Mode.DEBUG:
            show_image(level.name,image)
        elif Config().curent_mode() == Mode.LOG:
            log_image(level.name,image)
    except Exception as e:
        print(e)

def log_image(level,img):
    retval, buffer = cv2.imencode('.png', img)
    if not retval:
        return None
    html_logger.log_image(level,base64.b64encode(buffer).decode())


def show_image(title, img):
    cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    cv2.setWindowTitle('window', title)
    cv2.imshow('window', img)
    value = cv2.waitKey(0)
    if value == 27:
        os._exit(1)
    return value

def __init():
    global html_logger
    if Config().curent_mode()==Mode.LOG and html_logger is None:
        html_logger=hl.HtmlLogger(Config().log_path()+"/log.html")
