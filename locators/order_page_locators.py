from selenium.webdriver.common.by import By

class OrderLocators:

    ORDER_PAGE = [By.ID, 'root']
    NAME = [By.XPATH, ".//input[@placeholder= '* Имя']"]
    SURNAME = [By.XPATH, ".//input[@placeholder= '* Фамилия']"]
    ADDRESS = [By.XPATH, ".//input[@placeholder= '* Адрес: куда привезти заказ']"]
    PHONE_NUMBER = [By.XPATH, ".//input[@placeholder= '* Телефон: на него позвонит курьер']"]

    SUBWAY_STATION_FIELD = [By.XPATH, ".//input[@placeholder= '* Станция метро']"]
    SUBWAY_STATION_LST = [By.CLASS_NAME, 'select-search__options']
    SUBWAY_STATION = [By.XPATH, ".//li[@class = 'select-search__row']/button[@value = '8']/div[text() = 'Чистые пруды']"]

    RENT_FORM = [By.CLASS_NAME, 'Order_Form__17u6u']

    DELIVERY_TIME = [By.XPATH, ".//input[@placeholder= '* Когда привезти самокат']"]
    CALENDAR = [By.CLASS_NAME, 'react-datepicker__month']
    FIRST_DATE = [By.XPATH, ".//div[@class = 'react-datepicker__week']/div[@class = 'react-datepicker__day react-datepicker__day--001']"]
    LAST_DATE = [By.XPATH, ".//div[@class = 'react-datepicker__week']/div[@class = 'react-datepicker__day react-datepicker__day--031']"]

    RENT_PERIOD_FIELD = [By.CLASS_NAME, 'Dropdown-control']
    RENT_PERIOD_LST = [By.CLASS_NAME, 'Dropdown-menu']
    RENT_PERIOD_DAY = [By.CLASS_NAME, 'Dropdown-option']
    RENT_PERIOD_SEVEN_DAY = [By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'семеро суток']"]

    BLACK_PEARL = [By.XPATH, ".//input[@id='black']"]
    GRAY = [By.XPATH, "//input[@id='grey']"]

    COMMENT = [By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']"]

    NEXT_BUTTON = [By.XPATH, ".//div[@class = 'Order_NextButton__1_rCA']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    ORDER_BUTTON = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']"]

    CONFIRMATION_WINDOW = [By.CLASS_NAME, 'Order_Modal__YZ-d3']

    YES_BUTTON = [By.XPATH, ".//button[text() = 'Да']"]

    CREATE_ORDER_WINDOW = [By.CLASS_NAME, 'Order_Modal__YZ-d3']

    ORDER_TEXT = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']


