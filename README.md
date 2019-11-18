# opencv-log

[![CircleCI](https://img.shields.io/circleci/build/github/navarasu/opencv-log)](https://circleci.com/gh/navarasu/opencv-log) [![Coverage Status](https://img.shields.io/coveralls/github/navarasu/opencv-log/master)](https://coveralls.io/github/navarasu/opencv-log?branch=master) [![Pip Version](https://img.shields.io/pypi/v/opencv-log)](https://pypi.org/project/opencv-log) [![MIT License](https://img.shields.io/pypi/l/opencv-log)](https://github.com/navarasu/opencv-log/blob/master/LICENSE)

OpenCV based visual logger for debugging, logging and testing image processing code

## Usage

```python
import cvlog as log

os.environ['CVLOG_MODE'] = log.Mode.DEBUG
os.environ['CVLOG_LEVEL'] = log.Level.TRACE

img = cv2.imread("sample.img")

# log or show the image or do nothing based on current mode and current level
log.image(log.Level.INFO, img)

```

### Mode

* log.Mode.NONE (**Default**) - *Disable log and debug*
* log.Mode.LOG - *Log the image to interactive HTML to analyse the issue offline.*
* log.Mode.DEBUG - *Shows the image using cv2.imshow instead of logging to debug steps in development.*

```python
os.environ['CVLOG_MODE'] = log.Mode.LOG
```

### Level

* log.Mode.ERROR (**Default**) - *Log or Show only ERROR level.*
* log.Mode.TRACE - *Execute all log level steps.*
* log.Mode.INFO - *Execute only INFO and ERROR.*

```python
os.environ['CVLOG_LEVEL'] = log.Level.TRACE
```
