# Release notes

### [1.4.0](https://pypi.org/project/opencv-log/1.4.0/)
#### Compatible Release
* Compatible to all opencv version from 3.3 to latest

### [1.3.0](https://pypi.org/project/opencv-log/1.3.0/)
#### Log Types
* Differentiated logs by tagging log types like image, edges or contour
* Added to log threshold and edges as an alias to image
* Included option to log hough circles, keypoints, contours
* Log additional text content along with image, contour, etc

### [1.2.2](https://pypi.org/project/opencv-log/1.2.2/)
#### Log Rotation
* Option to rotate log for each run
* Option to config log path
* Support for windows
* Option to turn off log rotation

### [1.2.1](https://pypi.org/project/opencv-log/1.2.1/)
#### Log Houghlines
* Added option to log houghlines
* Fixed issue #7
* Improved test coverage
* Created seperate docs

### [1.1.0](https://pypi.org/project/opencv-log/1.1.0/)
#### Test Reporting
* Added option to report test result  multiple image to csv.
* Use cv2.imshow to show output image and save result based on input key


### [1.0.0](https://pypi.org/project/opencv-log/1.0.0/)
#### First Release
* Log image to HTML in LOG mode
* Use same logger to show image using cv2.imshow in DEBUG mode
* Disable logging in NONE mode
* Log or show based on log level TRACE, INFO and ERROR