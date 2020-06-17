Image
=====

.. code-block:: python

    import cvlog as log
    import cv2
    # Set default mode and level
    # If we dont set, then default mode is NONE
    # and the default level is ERROR

    log.set_mode(log.Mode.LOG)
    log.set_level(log.Level.TRACE)

    # image read using opencv

    img = cv2.imread("sample.png")

    # log or show the image or do nothing based on
    # the current mode and current level

    log.image(log.Level.INFO, img)

    log.image(log.Level.ERROR, img)

    log.image(log.Level.TRACE, img)


Threshold
=========

*This is just an alias to image to diffentiate log type in log list*

.. code-block:: python

    import cvlog as log
    import cv2
    img = cv2.imread('tests/data/board.jpg')
    log.set_mode(log.Mode.LOG)

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    log.threshold(log.Level.ERROR, thresh)

Edges
=====

.. code-block:: python

    import cvlog as log
    import cv2

    img = cv2.imread('tests/data/sudoku.png')
    log.set_mode(log.Mode.LOG)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    log.edges(log.Level.ERROR, edges)

.. note:: *Edges and Threshold are just an alias to image to diffentiate log type in log list*

.. image:: https://user-images.githubusercontent.com/20145075/84652210-e1cbbd80-af28-11ea-8f7b-11d574140809.png

Houghlines
==========

.. code-block:: python

    import cvlog as log
    import numpy as np
    import cv2

    img = cv2.imread('tests/data/sudoku.png')
    log.set_mode(log.Mode.LOG)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    # log or show the image by drawing the lines output
    log.hough_lines(log.Level.ERROR, lines, img)

HoughCircles
============

.. code-block:: python

    import cvlog as log
    import numpy as np
    import cv2

    img = cv2.imread('tests/data/board.jpg')
    log.set_mode(log.Mode.LOG)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)

    # log or show the image by drawing the circles output
    log.hough_circles(log.Level.ERROR, circles, img)

Contour
========

.. code-block:: python

    import cvlog as log
    import numpy as np
    import cv2

    img = cv2.imread('tests/data/contour.jpg')
    log.set_mode(log.Mode.LOG)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # log or show the image by drawing the all contour
    log.contours(log.Level.ERROR, contours, img)

    # log or show the image by drawing only first index contour
    log.contours(log.Level.ERROR, contours, img, 1)

Keypoints
==========

.. code-block:: python

    import cv2
    import cvlog as log

    img = cv2.imread('tests/data/orange.png')
    log.set_mode(log.Mode.LOG)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # feature key points from SIFT, SURF, FAST or ORB
    orb = cv2.ORB_create()
    kp, _ = orb.detectAndCompute(gray_img, None)

    # log or show the image with key points
    log.keypoints(log.Level.ERROR, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

Additional Params
=================

msg=
****
    *This optional parameter to log text message along with any log methods*

.. code-block:: python

    log.image(log.Level.ERROR, img, msg='Lorem ipsum dolor sit amet, ne persius reprehendunt mei.')

    log.contours(log.Level.ERROR, contours, img, msg='Lorem ipsum dolor sit amet, ne persius reprehendunt mei.')

    log.keypoints(log.Level.ERROR, kp, img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ,
                                           msg='Lorem ipsum dolor sit amet, ne persius reprehendunt mei.')

.. image:: https://user-images.githubusercontent.com/20145075/84654098-39b7f380-af2c-11ea-8860-09b38adaeac0.png