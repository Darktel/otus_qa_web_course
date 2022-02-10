from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CatalogPage(BasePage):
    path = 'index.php?route=product/category&path=20'

    SECTION_TITLE = (By.CSS_SELECTOR, "#content h2")
    SORT_BY = (By.CSS_SELECTOR, "#input-sort option:first-child")
    CART_BTN = (By.CSS_SELECTOR, "#cart")
    SHOW_BY = (By.CSS_SELECTOR, "#input-limit option[selected='selected']")
    PRODUCTS = (By.CSS_SELECTOR, "#content div:nth-child(7):not(.product-layout)")

    def open(self):
        self.url = self.url + self.path
        self.browser.get(self.url)
        return self

    def search_text_in_section_title(self, title_text):
        return self._element(self.SECTION_TITLE).text == title_text

    def check_property_section_title(self, property_element: str):
        return self._element(self.SORT_BY).get_property(property_element)

    def check_element_enable(self, selector: tuple):
        return self._element(selector).is_enabled()

    def check_default_value_show_by(self):
        return int(self._element(self.SHOW_BY).text)  # кол-во элементов на странице поумолчению.

    def check_count_product_in_page(self):
        '''кол-во элементов на странице меньше выставленного ограничения поумолчению.'''
        return len(self._element(self.PRODUCTS).find_elements(
                     By.CSS_SELECTOR, "div.product-layout")) < self.check_default_value_show_by()
