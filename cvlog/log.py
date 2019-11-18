import cv2
import os
import cvlog.html_logger as hl
import base64
from enum import Enum
Mode = Enum('Mode','DEBUG LOG NONE')
report_path="log"
html_logger,current_mode,current_level = None, None, None

class Level(Enum):
    TRACE = 1
    INFO = 2
    ERROR = 3

def image(level,image):
    #TODO log if null or invaild image data in log
    __init()
    if current_level.value > level.value:
        return
    if current_mode== Mode.DEBUG:
        show_image(level,image)
    elif current_mode == Mode.LOG:
        log_image(level,image)

def log_image(level,img):
    retval, buffer = cv2.imencode('.png', img)
    if not retval:
        return None
    html_logger.log_image(level,base64.b64encode(buffer).decode())
    

def show_image(level, img):
    cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    cv2.setWindowTitle('window', level.name)
    cv2.imshow('window', img)
    value = cv2.waitKey(0)
    if value == 27:
        os._exit(1)
    return value

def __init():
    global current_mode,html_logger,current_level
    if current_mode == None:
        current_mode=Mode[os.environ.get('CVLOG_MODE',"NONE")]
        current_level=Level[os.environ.get('CVLOG_LEVEL',"ERROR")]
        if current_mode==Mode.LOG:
            html_logger=hl.HtmlLogger(report_path+"/log.html")
    return  current_mode