from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import random, time
from Page_Object.MainPage import MainPage
from Page_Object.CatalogPage import CatalogPage
from Page_Object.ProductPage import ProductPage


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


def test_login_admin_page(browser, url):
    '''
    Страницу логина в админку /admin
    :param browser:
    '''
    # TODO: вынести елементы в отдельную страницу.

    browser.get(url + "/admin/")
    # TODO: вынеси логику теста в отдельнлый класс

    input_login = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "input-username")))
    assert input_login.get_attribute("placeholder") == "Username"
    # TODO: вынеси логику теста в отдельнлый класс

    input_password = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "input-password")))
    assert input_password.get_attribute("placeholder") == "Password"

    # TODO: вынеси логику теста в отдельнлый класс

    button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    assert button.get_property('type') == 'submit'
    assert button.text == 'Login'
    # TODO: вынеси логику теста в отдельнлый класс

    input_login.clear()
    input_login.send_keys('demo')
    input_password.clear()
    input_password.send_keys('demo')
    button.click()
    assert WebDriverWait(browser, 4).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#header > div > ul > li.dropdown > a"))).text == "demo demo"


@pytest.mark.parametrize('localor', (
        '#input-firstname', '#input-lastname', '#input-email', '#input-telephone', '#input-password', '#input-confirm'))
def test_registration_page(browser, url, localor):
    '''
    Страницу регистрации пользователя (/index.php?route=account/register)
    :param browser:
    '''
    # TODO: вынести елементы в отдельную страницу.

    browser.get(url + "/index.php?route=account/register")
    # TODO: вынеси логику теста в отдельнлый класс
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, localor))).is_displayed()


def test_registration_page_2(browser, url):
    '''
    Страницу регистрации пользователя (/index.php?route=account/register)
    :param browser:
    '''
    # TODO: вынести елементы в отдельную страницу.
    browser.get(url + "/index.php?route=account/register")
    # TODO: вынеси логику теста в отдельнлый класс
    assert WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h1"))).text == "Register Account"
    # TODO: вынеси логику теста в отдельнлый класс
    assert WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type=checkbox]:nth-child(2)"))).get_property(
        'type') == "checkbox"
