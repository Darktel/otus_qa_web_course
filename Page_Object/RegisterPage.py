from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from .BasePage import BasePage


class RegisterPage(BasePage):
    path = "index.php?route=account/register"
    TITLE_PAGE = (By.CSS_SELECTOR, "#content > h1")
    CHECK_BOX = (By.CSS_SELECTOR, "input[type=checkbox]:nth-child(2)")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    MESSAGE_SUCCESS_REGISTER = (By.CSS_SELECTOR, "#content > h1")

    TEST_USER = {
        "firstname": "Aleks",
        "lastname": "lex",
        "email": "test123@t2ee3est.ru",
        "telephone": "880033333333",
        "password": "qwerty",
        "confirm": "qwerty",
    }

    def open(self):
        self.url = self.url + self.path
        self.logger.info("Opening url: {}".format(self.url))
        with allure.step(f"Открывается страница {self.url}"):
            self.browser.get(self.url)
            self._click_alert()

    def check_element_in_page(self, _locator):
        with allure.step(f"Проверка наличия элемента на странице {_locator}"):
            return self._element((By.CSS_SELECTOR, _locator)).is_displayed()

    def check_text_in_header(self, value_text):
        with allure.step(f"Проверка что у элемента {self.TITLE_PAGE} текст {value_text}"):
            return self._element(self.TITLE_PAGE).text == value_text

    def check_property_check_box(self, value_property):
        try:
            return self._element(self.CHECK_BOX).get_property('type') == value_property
        except TimeoutException:
            raise AssertionError("Can't find element by locator: {}".format(self.CHECK_BOX))

    def _input_text(self, field, text):
        with allure.step(f"Ввод значения {text} в поле лемента {field}"):
            field = self._element(field)
            field.click()
            field.clear()
            field.send_keys(text)

    @allure.step("Создание нового пользователя")
    def create_new_user(self):
        for i in self.TEST_USER.keys():
            self._input_text((By.CSS_SELECTOR, f"input[name='{i}']"), self.TEST_USER[i])
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.PRIVACY_CHECKBOX)).click()
        WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    @allure.step("Проверка успешной регистрации")
    def check_success_register(self):
        return "Your Account Has Been Created!" in self._element(self.MESSAGE_SUCCESS_REGISTER).text
