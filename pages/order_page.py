from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators


class OrderPage(BasePage):

    def loading_order_page(self):
        return self.find_element_located(OrderLocators.ORDER_PAGE)

    def set_name(self, name):
        return self.find_element_located(OrderLocators.NAME).send_keys(name)

    def set_surname(self, surname):
        return self.find_element_located(OrderLocators.SURNAME).send_keys(surname)

    def set_address(self, address):
        return self.find_element_located(OrderLocators.ADDRESS).send_keys(address)

    def click_on_subway_station_field(self):
        return self.find_element_located_click(OrderLocators.SUBWAY_STATION_FIELD)

    def wait_for_subway_station_lst(self):
        return self.find_element_located(OrderLocators.SUBWAY_STATION_LST)

    def scroll_to_subway_station(self):
        subway_station = self.find_element_located(OrderLocators.SUBWAY_STATION)
        self.driver.execute_script("arguments[0].scrollIntoView();", subway_station)

    def choose_subway_station(self):
        return self.find_element_located_click(OrderLocators.SUBWAY_STATION)

    def set_phone_number(self, phone_number):
        return self.find_element_located(OrderLocators.PHONE_NUMBER).send_keys(phone_number)

    def click_on_next_button(self):
        return self.find_element_located_click(OrderLocators.NEXT_BUTTON)

    def loading_rent_form(self):
        return self.find_element_located(OrderLocators.RENT_FORM)

    def click_on_delivery_time_field(self):
        return self.find_element_located_click(OrderLocators.DELIVERY_TIME)

    def loading_month_calendar(self):
        return self.find_element_located(OrderLocators.CALENDAR)

    def choose_the_first_date(self):
        return self.find_element_located_click(OrderLocators.FIRST_DATE)

    def choose_the_last_date(self):
        return self.find_element_located_click(OrderLocators.LAST_DATE)

    def click_on_rent_period_field(self):
        return self.find_element_located_click(OrderLocators.RENT_PERIOD_FIELD)

    def loading_rent_period_lst(self):
        return self.find_element_located(OrderLocators.RENT_PERIOD_LST)

    def choose_rent_period_day(self):
        return self.find_element_located_click(OrderLocators.RENT_PERIOD_DAY)

    def scroll_to_rent_period_seven_day(self):
        rent_period_seven_day = self.find_element_located(OrderLocators.RENT_PERIOD_SEVEN_DAY)
        self.driver.execute_script("arguments[0].scrollIntoView();", rent_period_seven_day)

    def choose_rent_period_seven_day(self):
        return self.find_element_located_click(OrderLocators.RENT_PERIOD_SEVEN_DAY)

    def choose_black_scooter(self):
        return self.find_element_located_click(OrderLocators.BLACK_PEARL)

    def choose_gray_scooter(self):
        return self.find_element_located_click(OrderLocators.GRAY)

    def set_comment(self, comment):
        return self.find_element_located(OrderLocators.COMMENT).send_keys(comment)

    def click_to_complete_order(self):
        return self.find_element_located_click(OrderLocators.ORDER_BUTTON)

    def complete_order_form_through_up_order_button(self, name, surname, address, phone_number, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_on_subway_station_field()
        self.wait_for_subway_station_lst()
        self.scroll_to_subway_station()
        self.choose_subway_station()
        self.set_phone_number(phone_number)
        self.click_on_next_button()
        self.loading_rent_form()
        self.click_on_delivery_time_field()
        self.loading_month_calendar()
        self.choose_the_first_date()
        self.click_on_rent_period_field()
        self.loading_rent_period_lst()
        self.choose_rent_period_day()
        self.choose_black_scooter()
        self.set_comment(comment)
        self.click_to_complete_order()

    def complete_order_form_through_down_order_button(self, name, surname, address, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_on_subway_station_field()
        self.wait_for_subway_station_lst()
        self.scroll_to_subway_station()
        self.choose_subway_station()
        self.set_phone_number(phone_number)
        self.click_on_next_button()
        self.loading_rent_form()
        self.click_on_delivery_time_field()
        self.loading_month_calendar()
        self.choose_the_last_date()
        self.click_on_rent_period_field()
        self.loading_rent_period_lst()
        self.scroll_to_rent_period_seven_day()
        self.choose_rent_period_seven_day()
        self.choose_gray_scooter()
        self.click_to_complete_order()

    def loading_confirmation_window(self):
        return self.find_element_located(OrderLocators.CONFIRMATION_WINDOW)

    def click_on_yes_button(self):
        return self.find_element_located_click(OrderLocators.YES_BUTTON)

    def loading_create_order_window(self):
        return self.find_element_located(OrderLocators.CREATE_ORDER_WINDOW)

    def completion_of_the_order(self):
        self.loading_confirmation_window()
        self.click_on_yes_button()
        self.loading_create_order_window()

    def get_text_about_create_order(self):
        return self.find_element_located(OrderLocators.ORDER_TEXT).text

