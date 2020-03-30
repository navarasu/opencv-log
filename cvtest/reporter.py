from cvlog import log
from cvtest.csv_reporter import CsvReporter
from cvlog.config import Config
import traceback
import cv2
from uuid import uuid4
import os

class Reporter:
    def __new__(cls):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.__initialised = False
        return cls.instance

    def __init__(self):
        if not self.__initialised:
            self.__initialised = True
            report_path = Config().log_path() + "/report"
            self.image_path = report_path + '/images/'
            self.reporter = CsvReporter(report_path + "/report.csv")

    def result(self, input_image, key_pressed, output_img):
        message = ""
        if (key_pressed == ord("y")):
            result = "Pass"
        else:
            result = "Fail"
            message = self.__save_image(output_img)
        self.reporter.log_report([input_image, result.upper(), message])

    def __save_image(self, img):
        if not os.path.exists(self.image_path):
            os.makedirs(self.image_path)
        output_path = self.image_path + str(uuid4()) + '.png'
        cv2.imwrite(output_path, img)
        return output_path

    def error(self, input_image, ex):
        self.reporter.log_report([input_image, "ERROR", self.__stack_trace(ex)])

    def __stack_trace(self, ex):
        stacks = traceback.extract_tb(ex.__traceback__)[1:]
        stack_trace = ""
        for x in stacks[:10]:
            stack_trace += x.filename + ":" + str(x.lineno) + ";"
        return stack_trace

def report(input_image_path, processing_method):
    for image_path in input_image_path:
        try:
            img = processing_method(image_path)
            key_pressed = log.show_image(image_path, img)
        except Exception as e:
            Reporter().error(image_path, e)
        else:
            Reporter().result(image_path, key_pressed, img)
