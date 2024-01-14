import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainLocators
from constants import Constants
from constants import ResponseText


class TestQuestionPage:

    driver = None

    pay = (MainLocators.PAY_QUESTION, MainLocators.PAY_RESPONSE, ResponseText.PAY_RESPONSE_TEXT)
    quantity = (MainLocators.QUANTITY_QUESTION, MainLocators.QUANTITY_RESPONSE, ResponseText.QUANTITY_RESPONSE_TEXT)
    rent = (MainLocators.RENT_QUESTION, MainLocators.RENT_RESPONSE, ResponseText.RENT_RESPONSE_TEXT)
    order = (MainLocators.ORDER_QUESTION, MainLocators.ORDER_RESPONSE, ResponseText.ORDER_RESPONSE_TEXT)
    extend_and_return = (MainLocators.EXTEND_AND_RETURN_QUESTION,
                         MainLocators.EXTEND_AND_RETURN_RESPONSE, ResponseText.EXTEND_AND_RETURN_RESPONSE_TEXT)
    charger = (MainLocators.CHARGER_QUESTION, MainLocators.CHARGER_RESPONSE, ResponseText.CHARGER_RESPONSE_TEXT)
    cancel_order = (MainLocators.CANCEL_ORDER_QUESTION, MainLocators.CANCEL_ORDER_RESPONSE, ResponseText.CANCEL_ORDER_RESPONSE_TEXT)
    delivery = (MainLocators.DELIVERY_QUESTION, MainLocators.DELIVERY_RESPONSE, ResponseText.DELIVERY_RESPONSE_TEXT)

    @allure.title('Проверка появления ответа в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('question, response, answer_text', [pay, quantity, rent, order, extend_and_return, charger, cancel_order, delivery])
    def test_check_response_in_question(self, driver, question, response, answer_text):
        faq = MainPage(driver)
        faq.go_to_site(Constants.URL)
        faq.loading_main_page()
        faq.scroll_to_questions()
        faq.found_question(question)
        faq.click_on_question(question)
        faq.wait_for_response(response)
        response_text = faq.check_response(response)
        assert response_text == answer_text

