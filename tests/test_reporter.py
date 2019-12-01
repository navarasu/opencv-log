import cvtest as test
import cv2
from unittest.mock import patch
from .utils import read_file
from shutil import rmtree

@patch('cvlog.log.show_image')
def test_report_pass(show_image):
    rmtree('log/report')
    show_image.return_value=ord("y")
    test.report(['tests/data/orange.png'],process_image)
    assert read_file('log/report/report.csv') == 'Test Image,Result,Message\ntests/data/orange.png,PASS,\n'

@patch('cvlog.log.show_image')
def test_report_fail(show_image):
    show_image.return_value=ord("n")
    test.report(['tests/data/orange.png'],process_image)
    assert read_file('log/report/report.csv').startswith('Test Image,Result,Message\n'+
            'tests/data/orange.png,PASS,\n'+
            'tests/data/orange.png,FAIL,log/report/images/')

def test_report_error():
    test.report(['error.png'],process_image)
    result=read_file('log/report/report.csv')
    assert result.startswith('Test Image,Result,Message\n'+
            'tests/data/orange.png,PASS,\n'+
            'tests/data/orange.png,FAIL,log/report/images/')
    assert result.endswith('error.png,ERROR,/Users/navarasu/Workspace/opencv-log/tests/test_reporter.py:32;\n')

def process_image(image_path):
    if image_path == "error.png":
        raise Exception("Some exception in processing image")
    img = cv2.imread(image_path)
    return img

