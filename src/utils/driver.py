from appium import webdriver
from appium.options.android import UiAutomator2Options
from .readProperties import ReadConfig
from src.tests.conftest import get_dynamic_device_details


def get_driver():
    # Get dynamic device details (either from adb or BrowserStack)
    device_details = get_dynamic_device_details()

    # instance of ReadConfig
    config = ReadConfig()

    # Set up capabilities using the retrieved device details
    capabilities = {
        'browserstack.user': 'symonmuiruri_wx9NWQ',
        'browserstack.key': '6f6SSW5pz1B29bHus4Q5',
        'platformName': device_details['platformName'],
        'deviceName': device_details['deviceName'],
        'appPackage': ReadConfig().get_app_package(),  # From config.ini
        'appActivity': ReadConfig().get_app_activity(),  # From config.ini
        'noReset': ReadConfig().get_no_reset(),  # From config.ini
    }

    # Set up options with the desired capabilities
    options = UiAutomator2Options().load_capabilities(capabilities)
    # Determine the appropriate Appium server URL based on the environment (local or BrowserStack)
    if device_details['deviceType'] == 'Android Device':
        server_url = config.get_appium_server_url()
    else:
        server_url = config.get_browserstack_appium_server_url()

    # Initialize WebDriver with the selected Appium server URL and options
    driver = webdriver.Remote(server_url, options=options)

    return driver

