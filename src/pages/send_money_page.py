from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from src.utils.locators import SendMoneyLocators

class SendMoney:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)  # 50 seconds timeout

    def click_sendmoney(self):
        el_click_sendmoney = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.send_money_btn_XPATH)))
        el_click_sendmoney.click()

    def send_to_loopNumber(self):
        el_click_send_to_loop = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.send_to_loopNumber_XPATH)))
        el_click_send_to_loop.click()

    def choose_beneficiary(self):
        el_choose_beneficiary = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.select_beneficiary_XPATH)))
        el_choose_beneficiary.click()

    def enter_number(self, number):
        el_enter_number = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.mobile_number_XPATH)))
        el_enter_number.send_keys(number)

    def enter_amount(self, amount):
        el_enter_amount = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.enter_amount_XPATH)))
        el_enter_amount.send_keys(amount)

    def click_next(self):
        el_click_next = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.nextBtn_XPATH)))
        el_click_next.click()

    def select_loop_bank(self):
        el_select_loop_bank = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.loopBankAcc_XPATH)))
        el_select_loop_bank.click()

    def click_confirm(self):
        el_click_confirm = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.confirmBtn_XPATH)))
        el_click_confirm.click()

    def click_pay_now(self):
        el_click_pay_now = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.payNowBtn_XPATH)))
        el_click_pay_now.click()

    def enter_PIN(self, PIN):
        el_enter_pin = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.enterPIN_XPATH)))
        el_enter_pin.send_keys(PIN)

    def click_OK(self):
        el_click_ok = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, SendMoneyLocators.okBtn_XPATH)))
        el_click_ok.click()

    def is_send_successful(self):
        try:
            # Wait for the success message or indicator to be visible
            success_message = self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Transfer Success"]')))
            return success_message.is_displayed()
        except:
            return False
