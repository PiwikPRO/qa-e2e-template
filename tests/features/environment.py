from features.lib.pages import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def before_all(context):
     desired_cap = DesiredCapabilities.CHROME
     command_executor = 'http://selenium:4444/wd/hub'
     context.browser = webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_cap)


def after_all(context):
     context.browser.quit()
