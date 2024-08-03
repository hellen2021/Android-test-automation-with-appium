from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from src.utils.locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def is_logged_in(self):
        try:
             # Check if an element that appears only when logged in is present
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Hey,"]')))
            return True
        except:
            return False

    def enter_password(self, password):
        # print("password = ", LoginPageLocators.PASSWORD_FIELD_ID)
        el_text_password = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, LoginPageLocators.PASSWORD_FIELD_ID)))
        el_text_password.send_keys(password)

    def click_signin(self):
        el_signin_btn = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, LoginPageLocators.SIGNIN_BTN_ID)))
        el_signin_btn.click()

    def click_ok(self):
        el_btn_ok = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, LoginPageLocators.OK_BTN_ID)))
        el_btn_ok.click()

