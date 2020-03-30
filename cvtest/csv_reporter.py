import os
from shutil import rmtree
import csv

class CsvReporter:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__fields = ["Test Image", "Result", "Message"]
        self.__create_file()

    def __create_file(self):
        dir_path = os.path.dirname(self.__file_path)
        if os.path.exists(dir_path):
            rmtree(dir_path)
        os.makedirs(dir_path)
        with open(self.__file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.__fields)

    def __append(self, values):
        with open(self.__file_path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(values)

    def log_report(self, result):
        self.__append(result)
