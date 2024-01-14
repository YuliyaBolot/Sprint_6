from locators.dzen_page_locators import DzenLocators
from pages.base_page import BasePage

class DzenPage(BasePage):
    def loading_dzen_page(self):
        return self.find_element_located(DzenLocators.DZEN_PAGE)

