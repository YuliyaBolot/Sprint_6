import allure
import random
from pages.order_page import OrderPage
from pages.main_page import MainPage
from constants import Constants

class TestOrderPage:

    driver = None

    @allure.title('Проверка оформления заказа самоката через верхнюю кнопку "Заказать"')
    def test_make_order_through_up_order_button(self, driver):
        main = MainPage(driver)
        main.go_to_site(Constants.URL)
        main.loading_main_page()
        main.up_order_button()
        order = OrderPage(driver)
        order.loading_order_page()
        name = "Ян"
        surname = "Ли"
        address = "Ая д5"
        phone_number = f"{random.randint(1000000000, 9999999999999)}"
        order.complete_the_first_form(name, surname, address, phone_number)
        order.loading_rent_form()
        order.complete_delivery_time_field_with_first_date()
        order.complete_rent_period_field_with_day()
        order.choose_black_scooter()
        order.set_comment('Оставить у дома')
        order.click_to_complete_order()
        order.completion_of_the_order()
        create_order = order.get_text_about_create_order()
        assert Constants.ORDER_CONFIRMATION_TEXT in create_order

    @allure.title('Проверка оформления заказа самоката через нижнюю кнопку "Заказать"')
    def test_make_order_through_down_order_button(self, driver):
        main = MainPage(driver)
        main.go_to_site(Constants.URL)
        main.loading_main_page()
        main.click_on_cookie_button()
        main.scroll_to_down_order_button()
        main.click_on_down_order_button()
        order = OrderPage(driver)
        order.loading_order_page()
        name = "Габдельмуталлип"
        surname = "АбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиев"
        address = "Красный проспект, дом 154, корпус 2, квартира 102"
        phone_number = f"{random.randint(1000000000, 9999999999999)}"
        order.complete_the_first_form(name, surname, address, phone_number)
        order.loading_rent_form()
        order.complete_delivery_time_field_with_last_date()
        order.complete_rent_period_field_with_seven_day()
        order.choose_gray_scooter()
        order.click_to_complete_order()
        order.completion_of_the_order()
        create_order = order.get_text_about_create_order()
        assert Constants.ORDER_CONFIRMATION_TEXT in create_order


