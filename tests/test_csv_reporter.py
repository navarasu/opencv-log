from cvtest.csv_reporter import CsvReporter
from .utils import read_file, remove_dirs

csv_path = 'log/csv/'

def test_init_csv_reporter():
    remove_dirs(csv_path)
    CsvReporter(csv_path + 'test.csv')
    assert read_file(csv_path + 'test.csv') == 'Test Image,Result,Message\n'

def test_log_report():
    reporter = CsvReporter(csv_path + 'log.csv')
    reporter.log_report(['Image1', 'Fail', 'message'])
    assert read_file(csv_path + 'log.csv') == 'Test Image,Result,Message\nImage1,Fail,message\n'
