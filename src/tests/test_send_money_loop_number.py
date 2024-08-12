import pytest
import logging
from src.pages.send_money_page import SendMoney
from src.utils.driver import get_driver
from src.pages.login_page import LoginPage

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.regression
@pytest.mark.sanity
def test_send_money_loop_number(driver):
    # login page object
    login_page = LoginPage(driver)
    # send money object
    send_money_loop = SendMoney(driver)

    # Check if the user is already logged in
    if not login_page.is_logged_in():
        # If not logged in, perform the login steps
        login_page.enter_password('Test@123')
        login_page.click_signin()
        login_page.click_ok()

    # Assert that the user is logged in
    assert login_page.is_logged_in(), "Login failed"



    # proceed to send money
    send_money_loop.click_sendmoney()
    send_money_loop.send_to_loopNumber()

    print("Sent successfully")
    ''' 
    send_money_loop.choose_beneficiary()
    # send_money_loop.enter_number("0704540384")
    send_money_loop.enter_amount("80")
    send_money_loop.click_next()
    send_money_loop.select_loop_bank()
    send_money_loop.click_confirm()
    send_money_loop.click_pay_now()
    send_money_loop.enter_PIN("1234")
    send_money_loop.click_OK()

    # Verify that money has been sent successfully
    assert send_money_page.is_send_successful(), "Send money failed"

    # Initialize TestRailAPI
    testrail = TestrailApiClient(
        base_url="https://t24r17upgrade.testrail.io/index.php?/dashboard",
        user="Hellen.Cheptoo@ncbagroup.com",
        password="Rail@2023"
    )

    run_id = 1  # Test run ID
    case_id = 2  # Test case ID for send money test
    status_id = 1 if send_money_page.is_send_successful() else 5  # 1 for passed, 5 for failed
    comment = "Send money test passed" if send_money_page.is_send_successful() else "Send money test failed"

    # Send the result to TestRail
    result = testrail.add_result_for_case(run_id, case_id, status_id, comment)
    if result:
        logger.info(f"Result added to TestRail: {result}")
    else:
        logger.error("Failed to add result to TestRail")

'''


