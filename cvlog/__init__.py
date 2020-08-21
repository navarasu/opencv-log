from .logger import Logger
from .config import Level, Mode, set_mode, set_level, set_path, set_rotate_log

__all__ = ['Logger', 'image', 'edges', 'threshold', 'hough_circles', 'hough_lines', 'contours', 'keypoints', 'Level', 'Mode', 'set_mode', 'set_level', 'set_path', 'set_rotate_log']

root = Logger()
Logger.root = root

def image(level, image, **options):
    root.image(level, image, **options)

def edges(level, image, **options):
    root.edges(level, image, **options)

def threshold(level, image, **options):
    root.threshold(level, image, **options)

def hough_circles(level, lines, image, **options):
    root.hough_circles(level, lines, image, **options)

def hough_lines(level, circles, image, **options):
    root.hough_lines(level, circles, image, **options)

def contours(level, contours, image, index=-1, **options):
    root.contours(level, contours, image, index, **options)

def keypoints(level, kp, image, **options):
    root.keypoints(level, kp, image, **options)

def getLogger():
    return root
