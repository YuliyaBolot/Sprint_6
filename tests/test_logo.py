import allure
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from constants import Constants

class TestLogo:

    @allure.description('Проверка перехода на страницу Яндекс Дзена через логотип "Яндекс"')
    def test_yandex_logo(self, driver):
        yandex_logo = MainPage(driver)
        yandex_logo.go_to_site(Constants.URL)
        yandex_logo.click_on_yandex_logo()
        yandex_logo.switch_to_window()
        dzen = DzenPage(driver)
        dzen.loading_dzen_page()
        assert Constants.URL_DZEN in driver.current_url

    @allure.description('Проверка перехода на главную страницу «Самоката» через логотип "Самокат"')
    def test_scooter_logo(self, driver):
        scooter_logo = MainPage(driver)
        scooter_logo.go_to_site(Constants.URL_ORDER)
        scooter_logo.click_on_scooter_logo()
        scooter_logo.loading_main_page()
        assert Constants.URL == driver.current_url



