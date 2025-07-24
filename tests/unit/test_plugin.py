import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../../")
from pytest_html_reporter2.html_reporter import HTMLReporter  # noqa


def test_report_path():
    HTMLReporter.path = "."
    assert len(HTMLReporter.report_path.__get__(HTMLReporter)[0]) >= 5
    assert HTMLReporter.report_path.__get__(HTMLReporter)[1] == "pytest_html_report.html"

    HTMLReporter.path = "./report/test.html"
    assert len(HTMLReporter.report_path.__get__(HTMLReporter)[0]) >= 5
    assert HTMLReporter.report_path.__get__(HTMLReporter)[1] == "test.html"
