import cvlog as log
import cv2
import numpy as np
from .utils import read_file, remove_dirs, get_html

def test_log_image():
    remove_dirs('log/')
    img = cv2.imread("tests/data/orange.png")
    log.set_mode(log.Mode.LOG)
    log.image(log.Level.ERROR, img)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.log-type')[0].text == 'image'
    assert logitem[0]['logdata'] == read_file('tests/data/expected/image.txt')

def test_log_edges():
    remove_dirs('log/')
    img = cv2.imread('tests/data/sudoku.png')
    log.set_mode(log.Mode.LOG)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    log.edges(log.Level.ERROR, edges)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.log-type')[0].text == 'edges'
    assert logitem[0]['logdata'] == read_file('tests/data/expected/edges.txt')

def test_log_threshold():
    remove_dirs('log/')
    img = cv2.imread('tests/data/board.jpg')
    log.set_mode(log.Mode.LOG)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    log.threshold(log.Level.ERROR, thresh)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.log-type')[0].text == 'threshold'
    assert logitem[0]['logdata'] == read_file('tests/data/expected/thershold.txt')

def test_log_hough_lines():
    remove_dirs('log/')
    img = cv2.imread('tests/data/sudoku.png')
    log.set_mode(log.Mode.LOG)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    log.hough_lines(log.Level.ERROR, lines, img)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.log-type')[0].text == 'hough lines'
    assert logitem[0]['logdata'] == read_file('tests/data/expected/houghline_img.txt')

def test_log_hough_circles():
    remove_dirs('log/')
    img = cv2.imread('tests/data/board.jpg')
    log.set_mode(log.Mode.LOG)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)

    log.hough_circles(log.Level.ERROR, circles, img)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.log-type')[0].text == 'hough circles'
    assert logitem[0]['logdata'] == read_file('tests/data/expected/houghcircle_img.txt')

def test_contours():
    remove_dirs('log/')
    img = cv2.imread('tests/data/contour.jpg')
    log.set_mode(log.Mode.LOG)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    log.contours(log.Level.ERROR, contours, img)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.log-type')[0].text == 'contours'
    assert logitem[0]['logdata'] == read_file('tests/data/expected/contour.txt')

def test_keypoints():
    remove_dirs('log/')
    img = cv2.imread('tests/data/orange.png')
    log.set_mode(log.Mode.LOG)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    kp, _ = orb.detectAndCompute(gray_img, None)
    log.keypoints(log.Level.ERROR, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.log-type')[0].text == 'key points'
    print(logitem[0]['logdata'])
    # assert log_item[0]['logdata'] == read_file('tests/data/expected/keypoints.txt') #TODO Fix circle ci issue

def test_message():
    remove_dirs('log/')
    img = cv2.imread('tests/data/contour.jpg')
    log.set_mode(log.Mode.LOG)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    message = 'Lorem ipsum dolor sit amet, ne persius reprehendunt mei. Ea summo elitr munere his, et consul offendit recteque sea, quis elit nam ut.'
    log.image(log.Level.ERROR, img)
    log.contours(log.Level.ERROR, contours, img, msg=message)
    logitem = get_html('log/cvlog.html').select('.log-list .log-item')
    assert logitem[0].select('.description') == []
    assert logitem[1].select('.description')[0].text == message
