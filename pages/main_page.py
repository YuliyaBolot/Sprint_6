from pages.base_page import BasePage
from locators.main_page_locators import MainLocators

class MainPage(BasePage):

    def loading_main_page(self):
        return self.find_element_located(MainLocators.MAIN_PAGE)

    def click_on_cookie_button(self):
        return self.find_element_located_click(MainLocators.COOKIE_BUTTON)

    def click_on_up_order_button(self):
        return self.find_element_located_click(MainLocators.UP_ORDER_BUTTON)

    def up_order_button(self):
        self.click_on_cookie_button()
        self.click_on_up_order_button()

    def scroll_to_down_order_button(self):
        down_order_button = self.find_element_located(MainLocators.DOWN_ORDER_BUTTON, time=20)
        self.driver.execute_script("arguments[0].scrollIntoView();", down_order_button)

    def click_on_down_order_button(self):
        return self.find_element_located_click(MainLocators.DOWN_ORDER_BUTTON)

    def down_order_button(self):
        self.click_on_cookie_button()
        self.scroll_to_down_order_button()
        self.click_on_down_order_button()

    def click_on_yandex_logo(self):
        return self.find_element_located_click(MainLocators.LOGO_YANDEX)

    def click_on_scooter_logo(self):
        return self.find_element_located_click(MainLocators.LOGO_SCOOTER)

    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def scroll_to_questions(self):
        questions_lst = self.find_element_located(MainLocators.QUESTIONS_LST, time=20)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_lst)

    def found_question(self, question):
        return self.find_element_located(question, time=20)

    def click_on_question(self, question):
        return self.find_element_located_click(question)

    def wait_for_response(self, response):
        return self.find_element_located(response)

    def check_response(self, response):
        return self.find_element_located(response).text
