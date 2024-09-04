import os
import datetime


def save_screenshot(driver, test_name, folder='screenshots'):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Create the filename with timestamp and test name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    # Save the screenshot
    driver.save_screenshot(filepath)
    return filepath
