__author__ = 'mranjan'

import os
import csv
from utility.set_logging import logger


def generate_report(test_case, status,mode):
    try:
        report_path= os.path.join(os.path.dirname(os.getcwd()), 'reports')
        if os.path.exists(report_path):
            pass
        else:
            os.mkdir(report_path)
        report_file_path = os.path.join(os.path.dirname(os.getcwd()), 'reports', 'test_report.csv')
        if mode == "w":
            with open(report_file_path, mode) as report_file:
                csv_obj = csv.writer(report_file, delimiter=',', lineterminator='\n')
                csv_obj.writerow(["Test Cases", "Status"])
        else:
            with open(report_file_path, mode) as report_file:
                csv_obj = csv.writer(report_file, delimiter=',', lineterminator='\n')
                csv_obj.writerow([test_case, status])
    except FileNotFoundError as e:
        logger.error('Unable to write the report :'+str(e))
