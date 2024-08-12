from appium import webdriver
from appium.options.android import UiAutomator2Options
from .readProperties import ReadConfig
import pytest

'''def get_driver():
    capabilities = {
        'platformName': CONFIG['platformName'],
        'deviceName': CONFIG['deviceName'],
        'appPackage': CONFIG['appPackage'],
        'appActivity': CONFIG['appActivity'],
        'noReset': CONFIG['noReset']
    }

    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(CONFIG['appium_server_url'], options=options)
    return driver

'''
from appium import webdriver
from appium.options.android import UiAutomator2Options
from .readProperties import ReadConfig
from src.tests.conftest import get_dynamic_device_details


def get_driver():
    # Get dynamic device details (either from adb or BrowserStack)
    device_details = get_dynamic_device_details()

    # Set up capabilities using the retrieved device details
    capabilities = {
        'platformName': device_details['platformName'],
        'deviceName': device_details['deviceName'],
        'appPackage': ReadConfig().get_app_package(),  # From config.ini
        'appActivity': ReadConfig().get_app_activity(),  # From config.ini
        'noReset': ReadConfig().get_no_reset(),  # From config.ini
    }

    # Set up options with the desired capabilities
    options = UiAutomator2Options().load_capabilities(capabilities)

    # Initialize WebDriver with the Appium server URL and the options
    driver = webdriver.Remote(ReadConfig().get_appium_server_url(), options=options)

    return driver
