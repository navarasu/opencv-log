
<h1>
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://navarasu.github.io/opencv-log/assets/opencv-log-bl.png">
  <img height="80" src="https://navarasu.github.io/opencv-log/assets/opencv-log-wh.png">
</picture>
</h1>

[![Pypi
Version](https://img.shields.io/pypi/v/opencv-log.svg)](https://pypi.org/project/opencv-log) [![Build
Status](https://img.shields.io/circleci/build/github/navarasu/opencv-log)](https://circleci.com/gh/navarasu/opencv-log) [![Coverage
Status](https://img.shields.io/coveralls/github/navarasu/opencv-log/master)](https://coveralls.io/github/navarasu/opencv-log?branch=master) [![MIT
License](https://img.shields.io/pypi/l/opencv-log)](https://github.com/navarasu/opencv-log/blob/master/LICENSE)

An [OpenCV](https://opencv.org/) based visual logger for debugging,
logging and testing reporting an image processing code.

## Why opencv-log?

[![Visually Debug, Log and Test an Image Processing Code using OpenCV
and
Python](https://user-images.githubusercontent.com/20145075/81455232-3eaaba00-91ac-11ea-9213-7dd1c705f213.png)](https://blog.francium.tech/visually-debug-log-and-test-an-image-processing-code-using-opencv-and-python-36e2d944ebf2)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to
install.

``` sh
pip install opencv-log
```

**Documentation:** <https://navarasu.github.io/opencv-log>

## A Simple Usage

``` python
import cvlog as log
import cv2

# image read using opencv
img = cv2.imread("sample.png")

log.image(log.Level.ERROR, img)
```

Just by switching mode, you can use the same line of code for logging
and debugging. Also you can log houghlines, countour and more.

Refer [docs](https://navarasu.github.io/opencv-log) to get started.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

Refer
[Guidelines](https://github.com/navarasu/opencv-log/blob/master/CONTRIBUTION.md)
for more information.

## License

[MIT](https://choosealicense.com/licenses/mit/)
