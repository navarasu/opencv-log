import cvtest as test
import cv2
from unittest.mock import patch
from .utils import remove_dirs, ROOT_DIR
import csv
import os

report_path = 'log/report/report.csv'

@patch('cvlog.logger.BaseLogger.show_image')
def test_report_pass(show_image):
    remove_dirs('log/report/')
    show_image.return_value = ord("y")
    test.report(['tests/data/orange.png'], process_image)
    values = read_csv(report_path)
    assert len(values) == 2
    assert values[0] == ['Test Image', 'Result', 'Message']
    assert values[1] == ['tests/data/orange.png', 'PASS', '']

@patch('cvlog.logger.BaseLogger.show_image')
def test_report_fail(show_image):
    show_image.return_value = ord("n")
    test.report(['tests/data/orange.png'], process_image)
    values = read_csv(report_path)
    assert len(values) == 3
    assert values[-1][0] == 'tests/data/orange.png'
    assert values[-1][1] == 'FAIL'
    assert os.path.exists(values[-1][2]) is True

def test_report_error():
    test.report(['error.png'], process_image)
    values = read_csv(report_path)
    assert len(values) == 4
    assert values[-1][0] == 'error.png'
    assert values[-1][1] == 'ERROR'
    assert values[-1][2] == os.path.join(ROOT_DIR, 'tests', 'test_reporter.py:40;')

def process_image(image_path):
    if image_path == "error.png":
        raise Exception("Some exception in processing image")
    img = cv2.imread(image_path)
    return img

def read_csv(file_path):
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)
