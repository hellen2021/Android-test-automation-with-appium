import pytest
from src.utils.driver import get_driver
from src.pages.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.regression
def test_login(driver):
    login_page = LoginPage(driver)

    # Check if the user is already logged in
    if not login_page.is_logged_in():
        # If not logged in, perform the login steps
        login_page.enter_password('Test@123')
        login_page.click_signin()
        login_page.click_ok()

    # Assert that the user is logged in
    assert login_page.is_logged_in(), "Login failed"
    print("User already logged in")
