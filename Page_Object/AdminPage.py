from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AdminPage:
    path = "admin/"
    INPUT_LOGIN = (By.ID, "input-username")
    INPUT_PASSWORD = (By.ID, "input-password")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    HEADER_AUTHORIZATION_ADMIN = (By.CSS_SELECTOR, "#header > div > ul > li.dropdown > a")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url + self.path

    def open(self):
        self.browser.get(self.url)
        return self

    def check_attribute_input_login(self, value_attribute):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.INPUT_LOGIN)).get_attribute("placeholder") == value_attribute
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.INPUT_LOGIN))

    def check_attribute_password_login(self, value_attribute):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.INPUT_PASSWORD)).get_attribute("placeholder") == value_attribute
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.INPUT_PASSWORD))

    def check_property_button_submit(self, value_property):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.BUTTON_SUBMIT)).get_property('type') == value_property
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.BUTTON_SUBMIT))

    def check_text_button_submit(self, value_text):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.BUTTON_SUBMIT)).text == value_text
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(self.BUTTON_SUBMIT))

    def autorization_admin_page(self, login, password):
        input_login = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.INPUT_LOGIN))
        input_login.clear()
        input_login.send_keys(login)

        input_password = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.INPUT_PASSWORD))
        input_password.clear()
        input_password.send_keys(password)
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.BUTTON_SUBMIT)).click()
        return WebDriverWait(self.browser, 4).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#header > div > ul > li.dropdown > a"))).text
