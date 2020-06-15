import cv2
import os
import cvlog.html_logger as hl
import base64
import numpy as np
from cvlog.config import Config, Mode
html_logger = None

def image(level, image, **options):
    __image(level, 'image', image, options)

def edges(level, image, **options):
    __image(level, 'edges', image, options)

def threshold(level, image, **options):
    __image(level, 'threshold', image, options)

def hough_lines(level, lines, cv_image, **options):
    debug_image = cv_image.copy()
    for line in lines:
        (x1, y1), (x2, y2) = find_line_pts(line)
        cv2.line(debug_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    __image(level, 'hough lines', debug_image, options)

def hough_circles(level, circles, cv_image, **options):
    debug_image = cv_image.copy()
    if circles is not None:
        _a, b, _c = circles.shape
        for i in range(b):
            x, y, r = circles[0][i]
            cv2.circle(debug_image, (x, y), r, (0, 0, 255), 2)
            cv2.circle(debug_image, (x, y), 2, (0, 255, 0), 2)  # center
    __image(level, 'hough circles', debug_image, options)

def contours(level, contours, cv_image, index=-1, **options):
    debug_image = cv_image.copy()
    cv2.drawContours(debug_image, contours, index, (0, 255, 0), 2)
    __image(level, 'contours', debug_image, options)

def keypoints(level, kp, cv_image, **options):
    debug_image = cv_image.copy()
    cv2.drawKeypoints(debug_image, kp, debug_image, (0, 255, 0), flags=options.get('flags', 0))
    __image(level, 'key points', debug_image, options)

def find_line_pts(line):
    r, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * r
    y0 = b * r
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    return (x1, y1), (x2, y2)

def __image(level, log_type, image, options):
    if image is None:
        return
    __init()
    if Config().curent_level().value < level.value:
        return
    if Config().curent_mode() == Mode.DEBUG:
        show_image(level.name, log_type, image, options)
    elif Config().curent_mode() == Mode.LOG:
        log_image(level.name, log_type, image, options)

def log_image(level, log_type, img, options):
    retval, buffer = cv2.imencode('.png', img)
    if not retval:
        return None
    msg = options.get('msg', None)
    html_logger.log_image(level, log_type, base64.b64encode(buffer).decode(), msg)

def show_image(title, log_type, img, options):
    cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    cv2.setWindowTitle('window', title + ':' + log_type)
    cv2.imshow('window', img)
    value = cv2.waitKey(0)
    if value == 27:
        os._exit(1)
    return value

def __init():
    global html_logger
    if Config().curent_mode() == Mode.LOG and html_logger is None:
        html_logger = hl.HtmlLogger()
