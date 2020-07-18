## Logging \\ Debuging

```python
import cvlog as log
import cv2

# image read using opencv

img = cv2.imread("sample.png")

# Based on the log mode, the below line
# 1. Log the image to html (LOG mode) or
# 2. Show the image using cv2.imshow (DEBUG mode) or
# 3. Do Nothing (NONE mode)

log.image(log.Level.ERROR, img)
``` 

We can run this file `log_example.py` with three modes,

### Run in Log mode

```bash
CVLOG_MODE=LOG  python logging_example.py
```

This creates the image a interaractive html file `log\log.html`

![output](https://user-images.githubusercontent.com/20145075/84652724-b8f7f800-af29-11ea-9b15-2ce86640b629.png)

### Run in Debug mode

```sh
CVLOG_MODE=DEBUG  python logging_example.py
```

This shows the image using `cv2.imshow()`

![output](https://user-images.githubusercontent.com/20145075/78092636-e2ef5300-73ed-11ea-80f7-3a496388cc3d.png)

### Run in None\\OFF mode

```sh
python logging_example.py
```
This neither logs the image nor shows the image. 

## Testing Reporting

It is a semi automated and it automates only the reporting part. 
The validation part is done manually and we need to report the result by pressing 'y' or 'n' key.

**What it does?**

This shows processed output image using cv2.imshow that need to verified.

* On presssing 'y' key, it report it as PASS
* On pressing any other key, it report it as FAIL and save output image for verification
* On any exception, it report it as ERROR with exception stack

It generates CSV ot HTML report which can be used to for accuracy analysis.
By combining the log and test reporting, we can generate an interaractive html to debug and analyse the issue offline.

<!-- .. todo:: 
    HTML reporting is in milestone and it will be added in 1.6.0 version. -->


```python
 import cvtest as test
 import cv2

 # Example Process Image method from image path
 def process_image(imagepath):
    if imagepath == "error.png":
       raise Exception("Some exception in processing image")
    img = cv2.imread(imagepath)
    return img

 # List of the images path to be tested
 test_image_paths=["example1.png","example1.png","error.png"]

 # Run the test
 test.report(test_image_paths, process_image)
  ```
