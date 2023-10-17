from .logger import Logger
from .config import Level, Mode, set_mode, set_level, set_path, set_rotate_log

__all__ = ['Logger', 'image', 'edges', 'threshold', 'hough_circles', 'hough_lines', 'contours', 'keypoints', 'Level', 'Mode', 'set_mode', 'set_level', 'set_path', 'set_rotate_log']

root = Logger()
info = root.info
error = root.error
trace = root.trace
Logger.root = root

def getLogger(name=None):
    if name is None:
        return root


# LEGACY SUPPORT

def image(level, image, **options):
    getattr(root, level.name.lower()).image(image, **options)

def edges(level, image, **options):
    getattr(root, level.name.lower()).edges(image, **options)

def threshold(level, image, **options):
    getattr(root, level.name.lower()).threshold(image, **options)

def hough_circles(level, lines, image, **options):
    getattr(root, level.name.lower()).hough_circles(lines, image, **options)

def hough_lines(level, circles, image, **options):
    getattr(root, level.name.lower()).hough_lines(circles, image, **options)

def contours(level, contours, image, index=-1, **options):
    getattr(root, level.name.lower()).contours(contours, image, index, **options)

def keypoints(level, kp, image, **options):
    getattr(root, level.name.lower()).keypoints(kp, image, **options)
