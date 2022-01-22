from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage:
    HEADER_LINK = (By.ID, "top-links")
    ELEMENTS_OF_HEADER = (By.TAG_NAME, 'li')
    FREATURE_PRODUCT = (By.CLASS_NAME, "product-layout")
    BUTTON_CART = (By.CSS_SELECTOR, "#cart [type='button']")
    FOOTER_INFORMATION = (By.CSS_SELECTOR, "footer [class='list-unstyled'] [href]")
    SEARCH = (By.CSS_SELECTOR, "#search [name='search']")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        return self

    def search_elements_of_headers(self):
        try:
            return len(
                WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.HEADER_LINK)).find_elements(
                    *self.ELEMENTS_OF_HEADER))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.HEADER_LINK))

    def search_text_freature_product(self, text_product):
        try:
            return text_product in WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.FREATURE_PRODUCT)).text
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.FREATURE_PRODUCT))

    def search_tag_name_in_button_cart(self, tag_element):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.BUTTON_CART)).tag_name == tag_element
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.BUTTON_CART))

    def search_text_in_footer_information(self, text: str):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.FOOTER_INFORMATION)).text == text
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.FOOTER_INFORMATION))

    def search_tag_name_in_search_string(self, tag_element):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.SEARCH)).tag_name == tag_element
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.SEARCH))
