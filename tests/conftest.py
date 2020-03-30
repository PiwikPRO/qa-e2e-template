import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver():
     desired_cap = DesiredCapabilities.CHROME
     command_executor = 'http://selenium:4444/wd/hub'
     driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_cap)
     yield driver
     driver.quit()
