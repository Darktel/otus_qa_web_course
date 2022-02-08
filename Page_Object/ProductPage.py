from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .BasePage import BasePage

class ProductPage(BasePage):
    path = "index.php?route=product/product&path=20&product_id=44"

    NAME_PRODUCT = (By.CSS_SELECTOR, "#product-product > ul > li:last-child > a")
    # Тест проверки цены товара
    PRICE = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) h2")
    # Тест на доступность кнопки "Add to Cart"
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    BUTTON_COMPARE = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")
    ALERT_COMPARE = (By.CSS_SELECTOR, "#product-product > div.alert.alert-success.alert-dismissible")
    ALERT_MESSAGE_TO_COMPARE = 'Success: You have added MacBook Air to your product comparison!\n×'
    INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")



    def open(self):
        self.url = self.url + self.path
        self.browser.get(self.url)
        return self

    def check_name_product(self):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.NAME_PRODUCT)).text == 'MacBook Air'
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.NAME_PRODUCT))

    def check_price_product(self):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.PRICE)).text == '$1,202.00'
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.PRICE))

    def check_property_button_cart(self):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.BUTTON_CART)).get_property('type')
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.BUTTON_CART))

    def press_compare_button(self):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.element_to_be_clickable(self.BUTTON_COMPARE)).click()
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.BUTTON_COMPARE))

    def check_of_successful_addition_to_comparison(self):
        try:
            self._click_allert()
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.ALERT_COMPARE)).text == self.ALERT_MESSAGE_TO_COMPARE
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.ALERT_COMPARE))

    def add_to_cart(self, count_items: str):
            try:
                self._element_input = WebDriverWait(self.browser, 2).until(
                    EC.visibility_of_element_located(self.INPUT_QUANTITY))
                self._element_input.click()
                self._element_input.clear()
                self._element_input.send_keys(count_items)
                WebDriverWait(self.browser, 2).until(
                    EC.visibility_of_element_located(self.BUTTON_CART)).click()
            except TimeoutException:
                raise AssertionError(f"Cant find element by locator: {self.INPUT_QUANTITY}, or {self.BUTTON_CART}")

    def check_count_product_add_to_cart(self, count_product):
        try:
            return f'{count_product} item(s)' in WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.CART_TOTAL)).text
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.CART_TOTAL))
