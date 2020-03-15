import logging
import os
import time
from configparser import ConfigParser

import requests
from behave import use_fixture
from features.lib.pages import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from features.lib.pages import Api

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.getLogger("requests").setLevel(logging.WARNING)


def before_all(context):
    print("> Starting the browser")
    desired_cap = DesiredCapabilities.CHROME
    desired_cap['acceptInsecureCerts'] = True
    command_executor = 'http://selenium:4444/wd/hub'
    context.browser = webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_cap)
    context.browser.set_window_size(1920, 1080)


def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")


def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join('failed_scenarios_screenshots', 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
                                          + '_' + time.strftime("%H:%M:%S_%d_%m_%Y")
                                          + '.png')
        if context.browser.save_screenshot(scenario_file_path):
            print("> screenshot saved in: " + scenario_file_path)
        else:
            print("> failed to save screenshot")


def after_all(context):
    print("< Closing the browser")
    context.browser.quit()


def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
