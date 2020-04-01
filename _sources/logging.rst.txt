Logging an Image
================

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

Logging Houghlines
==================

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


Configuration
=============

Log Modes Options
#################

.. code-block:: python

    import cvlog as log
    log.set_mode(log.Mode.DEBUG)

Set mode using ENV variable

.. code-block:: python

    os.environ['CVLOG_MODE'] = "DEBUG"


+------------+------------------------------------------------------------------------+
| Mode.NONE  | | This is the default mode if we don't set mode.Used in production     |
|            | | It neither creates HTML file nor shows an image.                     |
+------------+------------------------------------------------------------------------+
| Mode.LOG   | Logs the image to interactive HTML to analyze the issue offline.       |
+------------+------------------------------------------------------------------------+
| Mode.DEBUG | | Shows the image using `cv2.imshow` instead of logging to debug steps |
|            | | in the development.It on move on to next log step on pressing any key|
|            | | and exit the code on pressing `ESC`.                                 |
+------------+------------------------------------------------------------------------+


Log Levels Options
##################

.. code-block:: python

    import cvlog as log
    log.set_level(log.Level.TRACE)

Set mode using ENV variable

.. code-block:: python

    os.environ['CVLOG_MODE'] = "TRACE"

+-------------+------------------------------------------------+
| Level.ERROR | Log or Show only ERROR level                   |
+-------------+------------------------------------------------+
| Level.INFO  | Log or Show INFO and ERROR level               |
+-------------+------------------------------------------------+
| Level.TRACE | Log or Show TRACE, INFO and ERROR level steps  |
+-------------+------------------------------------------------+

Level valid for DEBUG and LOG mode
