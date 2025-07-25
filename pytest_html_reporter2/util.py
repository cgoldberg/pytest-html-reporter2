import os
import shutil
import sys
from collections import Counter
from io import BytesIO

from PIL import Image

from pytest_html_reporter2.const_vars import ConfigVars


def suite_highlights(data):
    for i in data["content"]["suites"]:
        if data["content"]["suites"][i]["status"]["total_fail"] == 0:
            suite_name = data["content"]["suites"][i]["suite_name"]
            if suite_name not in ConfigVars.p_highlights:
                ConfigVars.p_highlights[suite_name] = 1
            else:
                ConfigVars.p_highlights[suite_name] += 1
        else:
            suite_name = data["content"]["suites"][i]["suite_name"]
            if suite_name not in ConfigVars.highlights:
                ConfigVars.highlights[suite_name] = 1
            else:
                ConfigVars.highlights[suite_name] += 1


def generate_suite_highlights():
    if ConfigVars.highlights == {}:
        ConfigVars.max_failure_suite_name_final = "No failures in History"
        ConfigVars.max_failure_suite_count = 0
        ConfigVars.max_failure_percent = "0"
        return

    ConfigVars.max_failure_suite_name = max(ConfigVars.highlights, key=ConfigVars.highlights.get)
    ConfigVars.max_failure_suite_count = ConfigVars.highlights[ConfigVars.max_failure_suite_name]

    if ConfigVars.max_failure_suite_name in ConfigVars.p_highlights:
        ConfigVars.max_failure_total_tests = (
            ConfigVars.p_highlights[ConfigVars.max_failure_suite_name] + ConfigVars.max_failure_suite_count
        )
    else:
        ConfigVars.max_failure_total_tests = ConfigVars.max_failure_suite_count

    ConfigVars.max_failure_percent = (ConfigVars.max_failure_suite_count / ConfigVars.max_failure_total_tests) * 100

    if ConfigVars.max_failure_suite_name.__len__() > 25:
        ConfigVars.max_failure_suite_name_final = ".." + ConfigVars.max_failure_suite_name[-23:]
    else:
        ConfigVars.max_failure_suite_name_final = ConfigVars.max_failure_suite_name

    res = Counter(ConfigVars.highlights.values())
    if max(res.values()) > 1:
        ConfigVars.similar_max_failure_suite_count = max(res.values())


def max_rerun():
    indices = [i for i, s in enumerate(sys.argv) if "reruns" in s]

    try:
        if "=" in sys.argv[int(indices[0])]:
            return int(sys.argv[int(indices[0])].split("=")[1])
        else:
            return int(sys.argv[int(indices[0]) + 1])
    except IndexError:
        return None


def screenshot(path=os.getcwd(), data=None):
    ConfigVars.screen_base = path
    ConfigVars.screen_img = Image.open(BytesIO(data))


def clean_screenshots(path):
    screenshot_dir = os.path.abspath(os.path.expanduser(os.path.expandvars(path))) + "/pytest_screenshots"
    if os.path.isdir(screenshot_dir):
        shutil.rmtree(screenshot_dir)


def custom_title(title):
    ConfigVars._title = title[:26] + "..." if title.__len__() > 29 else title
