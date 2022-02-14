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
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")

    def open(self):
        self.url = self.url + self.path
        self.logger.info("Opening url: {}".format(self.url))
        self.browser.get(self.url)
        return self

    def check_name_product(self):
        return self._element(self.NAME_PRODUCT).text == 'MacBook Air'

    def check_price_product(self):
        return self._element(self.PRICE).text == '$1,202.00'

    def check_property_button_cart(self):
        return self._element(self.BUTTON_CART).get_property('type')

    def press_compare_button(self):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.element_to_be_clickable(self.BUTTON_COMPARE)).click()
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.BUTTON_COMPARE))

    def check_of_successful_addition_to_comparison(self):
        try:
            self._click_alert()
            return self._element(self.ALERT_COMPARE).text == self.ALERT_MESSAGE_TO_COMPARE
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.ALERT_COMPARE))

    def add_to_cart(self, count_items: str):
        self._element_input = self._element(self.INPUT_QUANTITY)
        self._element_input.click()
        self._element_input.clear()
        self._element_input.send_keys(count_items)
        self._element(self.BUTTON_CART).click()

    def check_count_product_add_to_cart(self, count_product):
        return f'{count_product} item(s)' in self._element(self.CART_TOTAL).text
