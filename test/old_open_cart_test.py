from selenium.webdriver.common.by import By
import random, time
from Page_Object.MainPage import MainPage
from Page_Object.CatalogPage import CatalogPage
from Page_Object.ProductPage import ProductPage
from Page_Object.AdminPage import AdminPage
from Page_Object.RegisterPage import RegisterPage
import pytest, allure


def test_main_page(browser, url):
    '''
    Тесты на главную страницу url:https://demo.opencart.com/
    :param browser:
    :param url: 'https://demo.opencart.com/'
    '''
    main_page = MainPage(browser, url)
    main_page.open()
    # Проверка, что колличество элементов в верхней части страницы не изменяется = 7
    assert main_page.search_elements_of_headers() == 7
    # Проверка что первый элемент в избранном действительно macBook. (сталкивался с таким биз. требованием в реальности)
    assert main_page.search_text_freature_product('MacBook')
    # Поиск на странице кнопки Корзины.
    main_page.search_tag_name_in_button_cart('button')
    # Проверка футера страницы на наличие ссылки О Нас (About Us)
    assert main_page.search_text_in_footer_information('About Us')
    # Проверка строки поиска - у элемента строки поиска тег input (поле для ввода данных)
    assert main_page.search_tag_name_in_search_string('input')


@allure.title("Тест страницы категории товаров")
def test_catalog_page(browser, url):
    '''
    Тесты на каталог товаров - https://demo.opencart.com/index.php?route=product/category&path=20
    :param browser:
    '''
    cataog_page = CatalogPage(browser, url)
    cataog_page.open()
    assert cataog_page.search_text_in_section_title('Desktops')
    assert cataog_page.check_property_section_title('selected')
    assert cataog_page.check_element_enable((By.CSS_SELECTOR, "#cart"))
    assert cataog_page.check_default_value_show_by() == 15  # кол-во элементов на странице поумолчению.
    assert cataog_page.check_count_product_in_page()


@allure.title("Тест страницы категории товаров")
def test_product_card(browser, url):
    '''
    Карточку товара - https://demo.opencart.com/index.php?route=product/product&path=20&product_id=44
    :param browser:
    '''
    product_page = ProductPage(browser, url)
    product_page.open()
    # Тест на корректное наименование товара
    assert product_page.check_name_product()
    # Тест проверки цены товара
    assert product_page.check_price_product()
    # Тест на доступность кнопки "Add to Cart"
    assert product_page.check_property_button_cart() == 'button'
    # тест на успешное добавление товара в сравнение.
    product_page.press_compare_button()
    assert product_page.check_of_successful_addition_to_comparison
    # проверка верного кол-ва добавления товара в корзину.
    count_product = random.randint(1, 10)
    product_page.add_to_cart(str(count_product))  # Добавление товара в корзину
    time.sleep(1)
    product_page.check_count_product_add_to_cart(count_product)  # Проверка кол-ва товара добавленного в корзину.


@allure.title("Тест функционала авторизации через админку")
def test_login_admin_page(browser, url):
    '''
    Страницу логина в админку /admin
    :param browser:
    '''

    admin_page = AdminPage(browser, url)
    admin_page.open()
    assert admin_page.check_attribute_input_login("Username")
    assert admin_page.check_attribute_password_login("Password")
    assert admin_page.check_property_button_submit('submit')
    assert admin_page.check_text_button_submit('Login')
    assert admin_page.autorization_admin_page(login="user", password="bitnami") == "John Doe"


@allure.title("Тест наличия элементов на странице регистрации аккаунта")
@pytest.mark.parametrize('locator', (
        '#input-firstname', '#input-lastname', '#input-email', '#input-telephone', '#input-password', '#input-confirm'))
def test_registration_page(browser, url, locator):
    '''
    Страницу регистрации пользователя (/index.php?route=account/register)
    :param browser:
    '''
    register_page = RegisterPage(browser, url)
    register_page.open()
    assert register_page.check_element_in_page(locator)


@allure.title("Тестналичия элементов на странице регистрации аккаунта")
def test_registration_page_2(browser, url):
    '''
    Страницу регистрации пользователя (/index.php?route=account/register)
    :param browser:
    '''
    register_page = RegisterPage(browser, url)
    register_page.open()
    assert register_page.check_text_in_header("Register Account")
    assert register_page.check_property_check_box("checkbox")
