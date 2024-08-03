from appium import webdriver
from appium.options.android import UiAutomator2Options
from .config import CONFIG

def get_driver():
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
