import pytest

from src.pages import SendMoney
from src.utils.driver import get_driver
from src.pages.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.regression
@pytest.mark.sanity
def test_send_money_loop_number(driver):
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

    # proceed to send money
    send_money_loop = SendMoney(driver)
    send_money_loop.click_sendmoney()
    send_money_loop.send_to_loopNumber()
    send_money_loop.choose_beneficiary()
    # send_money_loop.enter_number("0704540384")
    send_money_loop.enter_amount("80")
    send_money_loop.click_next()
    send_money_loop.select_loop_bank()
    send_money_loop.click_confirm()
    send_money_loop.click_pay_now()
    send_money_loop.enter_PIN("1234")
    send_money_loop.click_OK()







