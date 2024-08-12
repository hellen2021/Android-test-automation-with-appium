import pytest
import logging
from src.utils.driver import get_driver
from src.pages.login_page import LoginPage
from src.utils.readProperties import ReadConfig
from src.tests.conftest import get_dynamic_device_details

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create an instance of ReadConfig
config = ReadConfig()

# Get the password from the configuration
password = config.get_password()

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.regression
def test_login(driver):
    login_page = LoginPage(driver)

    # Get device details dynamically
    device_details = get_dynamic_device_details()

    logger.info(f"Running tests on device: {device_details}")

    # Check if the user is already logged in
    if not login_page.is_logged_in():
        # If not logged in, perform the login steps
        login_page.enter_password(password)
        login_page.click_signin()
        login_page.click_ok()
        print("Login Successful !!!!")

    # Assert that the user is logged in
    assert login_page.is_logged_in(), "Login failed"
    print("User already logged in")
