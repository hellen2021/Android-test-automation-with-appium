class LoginPageLocators:
    SIGNIN_BTN_ID = "com.ncba.loop.test:id/btn_login"
    PASSWORD_FIELD_ID = "com.ncba.loop.test:id/et_input_box_content"
    OK_BTN_ID = "com.ncba.loop.test:id/btn_confirm"

class SendMoneyLocators:
    # locators common to all money channels : send to loop, mpesa ....
    send_money_btn_XPATH = '//android.widget.TextView[@text="Send Money"]'
    select_beneficiary_XPATH = '//android.widget.RelativeLayout[@resource-id="com.ncba.loop. \
                                test:id/rl_base_web"]/android.webkit.WebView/android.webkit.WebView/android. \
                                view.View[1]/android.view.View[2]/android.view.View[2]/android.view. \
                                View[1]/android.widget.TextView[1]'
    add_beneficiary_XPATH = '//android.widget.Image[@text="GxQBaAAAAAElFTkSuQmCC"]'
    mobile_number_XPATH = '//android.widget.EditText[@text="Enter your account number"]'
    enter_amount_XPATH = "//android.widget.EditText[@text='Enter amount']"
    nextBtn_XPATH = "//android.widget.Button[@text='Next']"
    walletAcc_XPATH = "//android.widget.ListView/android.view.View[1]"
    loopBankAcc_XPATH = "//android.widget.ListView/android.view.View[2]"
    activate_OD_now_XPATH = '//android.widget.TextView[@text="Activate now"]'
    confirmBtn_XPATH = "//android.widget.Button[@text='Confirm']"
    payNowBtn_XPATH = "//android.widget.Button[@text='Pay Now']"
    cancelBtn_XPATH = "//android.widget.Button[@text='Cancel']"
    enterPIN_XPATH = "//android.widget.EditText[@resource-id='com.ncba.loop.test:id/et_pin']"
    okBtn_XPATH = "//android.widget.Button[@text='OK']"


    # to mobile number
    # locators specific to each channel
    # to mobile loop number
    send_to_loopNumber_XPATH = "(//android.widget.TextView[@text='LOOP'])[1]"

    # mpesa
    send_to_mpesa_XPATH = '//android.widget.TextView[@text="MPESA"]'

    # pesalink
    # mobile number
    # next button







