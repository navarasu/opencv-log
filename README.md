# opencv-log

[![CircleCI](https://img.shields.io/circleci/build/github/navarasu/opencv-log)](https://circleci.com/gh/navarasu/opencv-log) [![Coverage Status](https://img.shields.io/coveralls/github/navarasu/opencv-log/master)](https://coveralls.io/github/navarasu/opencv-log?branch=master) [![Pip Version](https://img.shields.io/pypi/v/opencv-log)](https://pypi.org/project/opencv-log) [![MIT License](https://img.shields.io/pypi/l/opencv-log)](https://github.com/navarasu/opencv-log/blob/master/LICENSE)

OpenCV based visual logger for debugging, logging and testing image processing code

## Usage

```python
import cvlog as log

# Set default mode and level
# If we dont set, then default mode is NONE 
# and the default level is ERROR
log.set_mode(log.Mode.LOG)
log.set_level(log.Level.TRACE)

# image read using opencv

img = cv2.imread("sample.img")

# log or show the image or do nothing based on
# the current mode and current level


log.image(log.Level.INFO, img)

log.image(log.Level.ERROR, img)

log.image(log.Level.TRACE, img)

```

## Modes

```python
import cvlog as log
log.set_mode(log.Mode.DEBUG)

```

Set mode using ENV variable

```python
os.environ['CVLOG_MODE'] = "DEBUG"
```

### Mode.NONE (Default)

This is the default mode if we don't set mode.

Used in production. It neither creates HTML file nor shows an image.

### Mode.LOG

Logs the image to interactive HTML to analyze the issue offline.

![image](https://user-images.githubusercontent.com/20145075/69906004-ba752f00-13e2-11ea-8714-2425202148e8.png)

### Mode.DEBUG

Shows the image using `cv2.imshow` instead of logging to debug steps in the development. 

It on move on to next log step on pressing any key and exit the code on pressing `ESC`

![image](https://user-images.githubusercontent.com/20145075/69906116-581d2e00-13e4-11ea-8fbe-c1c5f778bb05.png)

## Levels

```python
import cvlog as log
log.set_level(log.Level.TRACE)
```

or

```python
os.environ['CVLOG_MODE'] = "TRACE"
```

* **Level.ERROR** (Default) - *Log or Show only ERROR level*
* **Level.INFO** - *Log or Show INFO and ERROR level*
* **Level.TRACE** - *Log or Show TRACE, INFO and ERROR level steps*
 
Level valid for DEBUG and LOG mode