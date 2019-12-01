# opencv-log

[![CircleCI](https://img.shields.io/circleci/build/github/navarasu/opencv-log)](https://circleci.com/gh/navarasu/opencv-log) [![Coverage Status](https://img.shields.io/coveralls/github/navarasu/opencv-log/master)](https://coveralls.io/github/navarasu/opencv-log?branch=master) [![Pip Version](https://img.shields.io/pypi/v/opencv-log)](https://pypi.org/project/opencv-log) [![MIT License](https://img.shields.io/pypi/l/opencv-log)](https://github.com/navarasu/opencv-log/blob/master/LICENSE)

OpenCV based visual logger for debugging, logging and testing image processing code

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install opencv-log
```

## Usage

### Log \ Debug

```python
import cvlog as log

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

```

### Test Report

```python
import cvtest as test

# Process Image from image path
def process_image(imagepath):
    if imagepath == "error.png":
        raise Exception("Some exception in processing image")
    img = cv2.imread(imagepath)
    return img

test_image_paths=["example1.png","example1.png","error.png"]

# This shows image using cv2.imshow,
# On presssing 'y' key, it report it as PASS
# On pressing any other key, it report it as FAIL and save output image for verification
# On any exception, it report it as ERROR with exception stack
test.report(test_image_paths, process_image)
```

## Log Modes

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

## Log Levels

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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
