from Page_Object.RegisterPage import RegisterPage
from Page_Object.MainPage import MainPage
import pytest
import allure


@allure.title("Тест смены отображаемой валюты на странице")
def test_switch_currency(browser, url, currency='EUR', currency_symbol='€'):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.change_currency(currency)
    assert main_page.check_selected_currency(currency_symbol)


@allure.title("Тест регистрации тестового пользователя")
def test_user_registration(browser, url):
    register_page = RegisterPage(browser, url)
    register_page.open()
    register_page.create_new_user()
    assert register_page.check_success_register()
