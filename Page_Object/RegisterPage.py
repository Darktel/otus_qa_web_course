from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegisterPage:
    path = "index.php?route=account/register"
    TITLE_PAGE = (By.CSS_SELECTOR, "#content > h1")
    CHECK_BOX = (By.CSS_SELECTOR, "input[type=checkbox]:nth-child(2)")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    MESSAGE_SUCCESS_REGISTER = (By.CSS_SELECTOR, "#content > h1")

    TEST_USER = {
        "firstname": "Aleks",
        "lastname": "lex",
        "email": "test123@teeest.ru",
        "telephone": "880033333333",
        "password": "qwerty",
        "confirm": "qwerty",
    }

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url + self.path

    def open(self):
        self.browser.get(self.url)
        return self

    def check_element_in_page(self, _locator):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, _locator))).is_displayed()
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(_locator))

    def check_text_in_header(self, value_text):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.TITLE_PAGE)).text == value_text
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.TITLE_PAGE))

    def check_property_check_box(self, value_property):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.CHECK_BOX)).get_property('type') == value_property
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.CHECK_BOX))

    def _input_text(self, field, text):
        field = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(field))
        field.click()
        field.clear()
        field.send_keys(text)
        try:
            self.browser.switch_to.alert.accept()
        except:
            pass

    def create_new_user(self):
        try:
            self.browser.switch_to.alert.accept()
        except:
            pass
        for i in self.TEST_USER.keys():
            self._input_text((By.CSS_SELECTOR, f"input[name='{i}']"), self.TEST_USER[i])
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.PRIVACY_CHECKBOX)).click()
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def check_success_register(self):
        try:
            return "Your Account Has Been Created!" in WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.MESSAGE_SUCCESS_REGISTER)).text
        except TimeoutException:
            raise AssertionError(f"Cant find element by locator: {self.MESSAGE_SUCCESS_REGISTER}")
