from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


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
        "email": "test123@tee3est.ru",
        "telephone": "880033333333",
        "password": "qwerty",
        "confirm": "qwerty",
    }

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url + self.path

    def open(self):
        with allure.step(f"Открывается страница {self.url}"):
            self.browser.get(self.url)
            try:
                self.browser.switch_to.alert.accept()
            except:
                pass


    def check_element_in_page(self, _locator):
        try:
            with allure.step(f"Проверка наличия элемента на странице {_locator}"):
                return WebDriverWait(self.browser, 2).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, _locator))).is_displayed()
        except TimeoutException:
            raise AssertionError("Can't find element by locator: {}".format(_locator))

    def check_text_in_header(self, value_text):
        try:
            with allure.step(f"Проверка что у элемента {self.TITLE_PAGE} текст {value_text}"):
                return WebDriverWait(self.browser, 2).until(
                    EC.visibility_of_element_located(self.TITLE_PAGE)).text == value_text
        except TimeoutException:
            raise AssertionError("Can't find element by locator: {}".format(self.TITLE_PAGE))

    def check_property_check_box(self, value_property):
        try:
            return WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.CHECK_BOX)).get_property('type') == value_property
        except TimeoutException:
            raise AssertionError("Can't find element by locator: {}".format(self.CHECK_BOX))


    def _input_text(self, field, text):
        with allure.step(f"Ввод значения {text} в поле лемента {field}"):
            field = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(field))
            field.click()
            field.clear()
            field.send_keys(text)
            try:
                self.browser.switch_to.alert.accept()
            except:
                raise AssertionError("Can't find input element in page")

    @allure.step("Создание нового пользователя")
    def create_new_user(self):
        for i in self.TEST_USER.keys():
            self._input_text((By.CSS_SELECTOR, f"input[name='{i}']"), self.TEST_USER[i])
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.PRIVACY_CHECKBOX)).click()
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    @allure.step("Проверка успешной регистрации")
    def check_success_register(self):
        try:
            return "Your Account Has Been Created!" in WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.MESSAGE_SUCCESS_REGISTER)).text
        except TimeoutException:
            raise AssertionError(f"Can't find element by locator: {self.MESSAGE_SUCCESS_REGISTER}")
