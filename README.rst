.. figure:: https://user-images.githubusercontent.com/20145075/78172497-c8f85380-7473-11ea-9eb6-8963fc879a42.png

.. image:: https://img.shields.io/pypi/v/opencv-log.svg
   :target: https://pypi.org/project/opencv-log
   :alt: Pypi Version 
.. image:: https://img.shields.io/circleci/build/github/navarasu/opencv-log
   :target: https://circleci.com/gh/navarasu/opencv-log
   :alt: Build Status
.. image:: https://img.shields.io/coveralls/github/navarasu/opencv-log/master
   :target: https://coveralls.io/github/navarasu/opencv-log?branch=master
   :alt: Coverage Status
.. image:: https://img.shields.io/pypi/l/opencv-log
   :target: https://github.com/navarasu/opencv-log/blob/master/LICENSE
   :alt: MIT License

|

An `OpenCV <https://opencv.org/>`_ based visual logger for debugging, logging and testing reporting an image processing code.

Why opencv-log?
###############

.. image:: https://user-images.githubusercontent.com/20145075/81455232-3eaaba00-91ac-11ea-9213-7dd1c705f213.png
   :target: https://blog.francium.tech/visually-debug-log-and-test-an-image-processing-code-using-opencv-and-python-36e2d944ebf2
   :alt: Visually Debug, Log and Test an Image Processing Code using OpenCV and Python

Installation
############
Use the package manager `pip <https://pip.pypa.io/en/stable/>`_ to install.

.. code-block:: sh

   pip install opencv-log


**Documentation:**  `<https://navarasu.github.io/opencv-log>`_

A Simple Usage
##############

.. code-block:: python

   import cvlog as log
   import cv2

   # image read using opencv
   img = cv2.imread("sample.png")

   log.image(log.Level.ERROR, img)

Just by switching mode, you can use the same line of code for logging and debugging. 
Also you can log houghlines, countour and more.

Refer `docs <https://navarasu.github.io/opencv-log>`_ to get started.

Contributing
############

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

License
#######

`MIT <https://choosealicense.com/licenses/mit/>`_
