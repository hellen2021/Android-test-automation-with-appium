import pytest
import subprocess
import logging

from py.xml import html
from src.utils.readProperties import ReadConfig

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the configuration reader
config_reader = ReadConfig()

def is_device_connected():
    # Check if there is any device connected using adb
    devices_output = subprocess.getoutput("adb devices").strip().splitlines()
    # The first line is the header, so we skip it
    connected_devices = [line for line in devices_output if "device" in line and not line.startswith("List")]
    return len(connected_devices) > 0

def get_dynamic_device_details():
    if is_device_connected():
        logger.info("Connected device detected. Fetching details using adb...")
        # Fetch details using adb if a device is connected
        device_name = subprocess.getoutput("adb shell getprop ro.product.model").strip()
        platform_version = subprocess.getoutput("adb shell getprop ro.build.version.release").strip()
        platform_sdk_version = subprocess.getoutput("adb shell getprop ro.build.version.sdk").strip()

        return {
            "deviceName": device_name,
            "platformName": "Android",
            "platformVersion": platform_version,
            "sdk_version": platform_sdk_version,
            "deviceType": "Android Device"
        }
    else:
        logger.info("No connected device detected. Falling back to BrowserStack emulator details.")
        # Fallback to BrowserStack emulator details from the YAML configuration
        try:
            desired_capabilities = config_reader.get_device_capabilities(0)  # Adjust the index if necessary
            return {
                "deviceName": desired_capabilities['deviceName'],
                "platformName": desired_capabilities['platformName'],
                "platformVersion": desired_capabilities['platformVersion'],
                "deviceType": "Android Emulator (BrowserStack)",
            }
        except Exception as e:
            logger.error(f"Failed to fetch BrowserStack device details: {e}")
            raise

# Hook to add metadata to the HTML report
def pytest_configure(config):
    device_details = get_dynamic_device_details()
    config._metadata["Device Type"] = device_details["deviceType"]
    config._metadata["Device Name"] = device_details["deviceName"]
    config._metadata["Platform Name"] = device_details["platformName"]
    config._metadata["Platform Version"] = device_details["platformVersion"]

# Hook to add a summary to the HTML report
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    device_details = get_dynamic_device_details()
    terminalreporter.section("Device Summary")
    terminalreporter.write_line(f"Tests executed on: {device_details['deviceType']}")
    terminalreporter.write_line(f"Device Name: {device_details['deviceName']}")
    terminalreporter.write_line(f"Platform Name: {device_details['platformName']}")
    terminalreporter.write_line(f"Platform Version: {device_details['platformVersion']}")

# Hook to modify the HTML report summary
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    device_details = get_dynamic_device_details()
    summary.extend([html.p("Device Summary:")])
    summary.extend([html.ul(
        html.li(f"Device Type: {device_details['deviceType']}"),
        html.li(f"Device Name: {device_details['deviceName']}"),
        html.li(f"Platform Name: {device_details['platformName']}"),
        html.li(f"Platform Version: {device_details['platformVersion']}")
    )])


'''
import pytest
import subprocess
from py.xml import html

def get_device_details():
    device_name = subprocess.getoutput("adb shell getprop ro.product.model").strip()
    android_version = subprocess.getoutput("adb shell getprop ro.build.version.release").strip()
    platform_name = subprocess.getoutput("adb shell getprop ro.build.version.sdk").strip()

    return {
        "deviceName": device_name,
        "platformName": platform_name,
        "androidVersion": android_version,
    }


# Hook to add metadata to the HTML report
def pytest_configure(config):
    device_details = get_device_details()
    config._metadata["Device Type"] = "Android Device"
    config._metadata["Device Name"] = device_details["deviceName"]
    config._metadata["Platform Name"] = device_details["platformName"]
    config._metadata["Android Version"] = device_details["androidVersion"]


# Hook to add a summary to the HTML report
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    device_details = get_device_details()
    terminalreporter.section("Device Summary")
    terminalreporter.write_line("Tests executed on: Android Device")
    terminalreporter.write_line(f"Device Name: {device_details['deviceName']}")
    terminalreporter.write_line(f"Android Version: {device_details['androidVersion']}")
    terminalreporter.write_line(f"Platform Name: {device_details['platformName']}")


# Hook to modify the HTML report summary
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    device_details = get_device_details()
    summary.extend([html.p("Device Summary:")])
    summary.extend([html.ul(
        html.li("Device Type: Android Device"),
        html.li(f"Device Name: {device_details['deviceName']}"),
        html.li(f"Android Version: {device_details['androidVersion']}")

    )])
'''
