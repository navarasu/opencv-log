## Set Log Mode

``` python
import cvlog as log
log.set_mode(log.Mode.DEBUG)
```

Set mode using ENV variable

``` sh
CVLOG_MODE=DEBUG  python logging_example.py
```

``` python
os.environ['CVLOG_MODE'] = "DEBUG"
```
|             |                                               |
| ----------- | --------------------------------------------- |
| Mode.NONE  | This is the default mode if we don't set mode.Used in production. <br>It neither creates HTML file nor shows an image.|
| Mode.LOG   | Logs the image to interactive HTML to analyze the issue offline.<br> 
| Mode.DEBUG | Shows the image using `cv2.imshow` instead of logging to debug steps <br>in the development.It on move on to next log step on pressing any key <br>and exit the code on pressing `ESC`.|


## Set Log Level

``` python
import cvlog as log
log.set_level(log.Level.TRACE)
```

Set mode using ENV variable

``` sh
CVLOG_LEVEL=TRACE  python logging_example.py
```

``` python
os.environ['CVLOG_LEVEL'] = "TRACE"
```

|             |                                               |
| ----------- | --------------------------------------------- |
| Level.ERROR | Log or Show only ERROR level                  |
| Level.INFO  | Log or Show INFO and ERROR level              |
| Level.TRACE | Log or Show TRACE, INFO and ERROR level steps |

Level valid for DEBUG and LOG mode

## Change Log Path

``` python
import cvlog as log
log.set_path("folder_path")
```

Set mode using ENV variable

``` sh
CVLOG_PATH=folder_path  python logging_example.py
```

``` python
os.environ['CVLOG_PATH'] = "folder_path"
```

## Disable Log Rotation

``` python
import cvlog as log
log.set_rotate_log(False)
```