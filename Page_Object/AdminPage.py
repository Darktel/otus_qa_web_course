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
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog")
    CATALOG_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, ".page-header .pull-right a.btn")
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    TAB_DATA = (By.CSS_SELECTOR, "a[href='#tab-data']")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "#form-product table")
    BUTTON_SAVE = (By.CSS_SELECTOR, "button[type='submit']")

    FILTER_PRODUCT = (By.CSS_SELECTOR, '#input-name')
    BUTTON_FILTER_SUBMIT = (By.CSS_SELECTOR, '#button-filter')
    CHECK_BOX_PRODUCTS = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, ".page-header .pull-right button.btn-danger")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

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

    def open_products_list(self):
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CATALOG_MENU)).click()
        WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable(self.CATALOG_PRODUCTS_BUTTON)).click()

    def add_new_product(self, product_name):
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.ADD_NEW_BUTTON)).click()
        _input_product = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.INPUT_PRODUCT_NAME))
        _input_product.click()
        _input_product.clear()
        _input_product.send_keys(product_name)
        _input_tag = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.META_TAG_TITLE_INPUT))
        _input_tag.click()
        _input_tag.clear()
        _input_tag.send_keys("auto Tesla")
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.TAB_DATA)).click()
        _input_model = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.MODEL_INPUT))
        _input_model.click()
        _input_model.clear()
        _input_model.send_keys("test tesla")
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.BUTTON_SAVE)).click()
        return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.SUCCESS_ALERT)).is_displayed()

    def delete_product(self):
        # TODO: сделать фильтрацию по товару.
        _input_product = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FILTER_PRODUCT))
        _input_product.click()
        _input_product.clear()
        _input_product.send_keys('Tesla')
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.BUTTON_FILTER_SUBMIT)).click()

        # TODO: ткнуть чек-бокс, и удалить товар.

        assert len(WebDriverWait(self.browser, 2).until(
            EC.visibility_of_all_elements_located(self.CHECK_BOX_PRODUCTS))) > 1, 'Нет товара для удаления.'
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CHECK_BOX_PRODUCTS)).click()
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.DELETE_BUTTON)).click()
        self.browser.switch_to.alert.accept()
        return WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT)).text == 'Success: You have modified products!'
