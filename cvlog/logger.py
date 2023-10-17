import cv2
import os
import cvlog.html_logger as hl
import base64
import numpy as np
from cvlog.config import Config, Mode, Level

class Logger:
    root = None

    def __init__(self, name=None):
        self.error = BaseLogger(Level.ERROR, name)
        self.info = BaseLogger(Level.INFO, name)
        self.trace = BaseLogger(Level.TRACE, name)

class BaseLogger:
    root = None

    def __init__(self, level=None, name=None):
        self.__name = name
        self.__level = level
        self.__html_logger = hl.HtmlLogger()

    def image(self, image, **options):
        self.__image('image', image, options)

    def edges(self, image, **options):
        self.__image('edges', image, options)

    def threshold(self, image, **options):
        self.__image('threshold', image, options)

    def hough_lines(self, lines, cv_image, **options):
        debug_image = cv_image.copy()
        for line in lines:
            (x1, y1), (x2, y2) = self.__find_line_pts(line)
            cv2.line(debug_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        self.__image('hough lines', debug_image, options)

    def hough_circles(self, circles, cv_image, **options):
        debug_image = cv_image.copy()
        if circles is not None:
            _a, b, _c = circles.shape
            for i in range(b):
                x, y, r = circles[0][i]
                cv2.circle(debug_image, (x, y), r, (0, 0, 255), 2)
                cv2.circle(debug_image, (x, y), 2, (0, 255, 0), 2)  # center
        self.__image('hough circles', debug_image, options)

    def contours(self, contours, cv_image, index=-1, **options):
        debug_image = cv_image.copy()
        cv2.drawContours(debug_image, contours, index, (0, 255, 0), 2)
        self.__image('contours', debug_image, options)

    def keypoints(self, kp, cv_image, **options):
        debug_image = cv_image.copy()
        cv2.drawKeypoints(debug_image, kp, debug_image, (0, 255, 0), flags=options.get('flags', 0))
        self.__image('key points', debug_image, options)

    def __find_line_pts(self, line):
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

    def __image(self, log_type, image, options):
        if image is None:
            return
        if Config().curent_level().value < self.__level.value:
            return
        if Config().curent_mode() == Mode.DEBUG:
            self.show_image(self.__level.name, log_type, image, options)
        elif Config().curent_mode() == Mode.LOG:
            self.__log_image(self.__level.name, log_type, image, options)

    def __log_image(self, level, log_type, img, options):
        retval, buffer = cv2.imencode('.png', img)
        if not retval:
            return None
        msg = options.get('msg', None)
        self.__html_logger.log_image(level, self.__name, log_type, base64.b64encode(buffer).decode(), msg)

    def show_image(self, title, log_type, img, options):
        cv2.namedWindow('window', cv2.WINDOW_NORMAL)
        cv2.setWindowTitle('window', title + ':' + log_type)
        cv2.imshow('window', img)
        value = cv2.waitKey(0)
        if value == 27:
            os._exit(1)
        return value
