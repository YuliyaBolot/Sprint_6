from selenium.webdriver.common.by import By

class MainLocators:

    MAIN_PAGE = [By.CLASS_NAME, 'Home_HomePage__ZXKIX']

    UP_ORDER_BUTTON = [By.XPATH, ".//button[@class = 'Button_Button__ra12g']"]

    DOWN_ORDER_BUTTON = [By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']/button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']"]

    LOGO_YANDEX = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    LOGO_SCOOTER = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    COOKIE_BUTTON = [By.ID, 'rcc-confirm-button']

    QUESTIONS_LST = [By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']/div[@class = 'accordion']"]

    PAY_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-0']"]
    PAY_RESPONSE = [By.ID, 'accordion__panel-0']

    QUANTITY_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-1']"]
    QUANTITY_RESPONSE = [By.ID, 'accordion__panel-1']

    RENT_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-2']"]
    RENT_RESPONSE = [By.ID, 'accordion__panel-2']

    ORDER_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-3']"]
    ORDER_RESPONSE = [By.ID, 'accordion__panel-3']

    EXTEND_AND_RETURN_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-4']"]
    EXTEND_AND_RETURN_RESPONSE = [By.ID, 'accordion__panel-4']

    CHARGER_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-5']"]
    CHARGER_RESPONSE = [By.ID, 'accordion__panel-5']

    CANCEL_ORDER_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-6']"]
    CANCEL_ORDER_RESPONSE = [By.ID, 'accordion__panel-6']

    DELIVERY_QUESTION = [By.XPATH, ".//div[@class = 'accordion__item']//div[@id = 'accordion__heading-7']"]
    DELIVERY_RESPONSE = [By.ID, 'accordion__panel-7']


