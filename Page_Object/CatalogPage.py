from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .BasePage import BasePage


class CatalogPage:
    path = 'index.php?route=product/category&path=20'

    SECTION_TITLE = (By.CSS_SELECTOR, "#content h2")
    SORT_BY = (By.CSS_SELECTOR, "#input-sort option:first-child")
    CART_BTN = (By.CSS_SELECTOR, "#cart")
    SHOW_BY = (By.CSS_SELECTOR, "#input-limit option[selected='selected']")
    PRODUCTS = (By.CSS_SELECTOR, "#content div:nth-child(7):not(.product-layout)")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url + self.path

    def open(self):
        self.browser.get(self.url)
        return self

    def search_text_in_section_title(self, title_text):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.SECTION_TITLE)).text == title_text
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.SECTION_TITLE))

    def check_property_section_title(self, property_element: str):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.SORT_BY)).get_property(property_element)
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.SORT_BY))

    def check_element_enable(self, selector: tuple):
        try:
            return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(selector)).is_enabled()
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(selector))

    def check_default_value_show_by(self):
        try:
            return int(WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.SHOW_BY)).text)  # кол-во элементов на странице поумолчению.
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.SHOW_BY))

    def check_count_product_in_page(self):
        try:
            return len(WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PRODUCTS)).find_elements(
                By.CSS_SELECTOR,
                "div.product-layout")) < self.check_default_value_show_by()  # кол-во элементов на странице поумолчению.
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.PRODUCTS))
