from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .BasePage import BasePage


class MainPage(BasePage):
    HEADER_LINK = (By.ID, "top-links")
    ELEMENTS_OF_HEADER = (By.TAG_NAME, 'li')
    FREATURE_PRODUCT = (By.CLASS_NAME, "product-layout")
    BUTTON_CART = (By.CSS_SELECTOR, "#cart [type='button']")
    FOOTER_INFORMATION = (By.CSS_SELECTOR, "footer [class='list-unstyled'] [href]")
    SEARCH = (By.CSS_SELECTOR, "#search [name='search']")
    CURRENCY_LOCATOR = (By.CSS_SELECTOR, "#top .btn-group")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top .btn-group .dropdown-menu")
    SELECTED_CURRENCY = (By.CSS_SELECTOR, "button.btn-link strong")

    def open(self):
        self.logger.info("Opening url: {}".format(self.url))
        self.browser.get(self.url)
        return self

    def search_elements_of_headers(self):
        return len(self._element(self.HEADER_LINK).find_elements(*self.ELEMENTS_OF_HEADER))

    def search_text_freature_product(self, text_product):
        return text_product in self._element(self.FREATURE_PRODUCT).text

    def search_tag_name_in_button_cart(self, tag_element):
        return self._element(self.BUTTON_CART).tag_name == tag_element

    def search_text_in_footer_information(self, text: str):
        return self._element(self.FOOTER_INFORMATION).text == text

    def search_tag_name_in_search_string(self, tag_element):
        return self._element(self.SEARCH).tag_name == tag_element

    def change_currency(self, currency):
        try:
            WebDriverWait(self.browser, 2).until(
                EC.element_to_be_clickable(self.CURRENCY_LOCATOR)).click()
            WebDriverWait(self.browser, 2).until(
                EC.element_to_be_clickable(self.CURRENCY_DROPDOWN))
            self._element((By.CSS_SELECTOR, f".currency-select[name='{currency}']")).click()

        except TimeoutException:
            raise AssertionError(f"Cant find element by locator: {self.CURRENCY_LOCATOR}")

    def check_selected_currency(self, text_currency):
        return text_currency in self._element(self.SELECTED_CURRENCY).text
