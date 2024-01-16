import allure
import random
from pages.order_page import OrderPage
from pages.main_page import MainPage
from constants import Constants

class TestOrderPage:

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
        comment = 'Оставить у дома'
        order.complete_order_form_through_up_order_button(name, surname, address, phone_number, comment)
        order.completion_of_the_order()
        create_order = order.get_text_about_create_order()
        assert Constants.ORDER_CONFIRMATION_TEXT in create_order

    @allure.title('Проверка оформления заказа самоката через нижнюю кнопку "Заказать"')
    def test_make_order_through_down_order_button(self, driver):
        main = MainPage(driver)
        main.go_to_site(Constants.URL)
        main.loading_main_page()
        main.down_order_button()
        order = OrderPage(driver)
        order.loading_order_page()
        name = "Габдельмуталлип"
        surname = "АбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиевАбдуллагаджиев"
        address = "Красный проспект, дом 154, корпус 2, квартира 102"
        phone_number = f"{random.randint(1000000000, 9999999999999)}"
        order.complete_order_form_through_down_order_button(name, surname, address, phone_number)
        order.completion_of_the_order()
        create_order = order.get_text_about_create_order()
        assert Constants.ORDER_CONFIRMATION_TEXT in create_order


