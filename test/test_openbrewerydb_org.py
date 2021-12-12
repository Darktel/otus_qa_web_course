import pytest
import requests
import cerberus

BASE_URL = 'https://api.openbrewerydb.org/breweries'


class Test_api():
    '''Тестирование REST сервиса 2 Написать минимум 5 тестов для REST API сервиса: https://www.openbrewerydb.org/.
     Как минимум 2 из 5 должны использовать параметризацию. Документация к API есть на сайте. Тесты должны успешно проходить.
    '''

    def test_status(self):
        response = requests.get(BASE_URL)
        assert response.status_code == 200, 'false request'

    @pytest.mark.parametrize('name', ['10-56 Brewing Company', '12 Acres Brewing Company', "12 Gates Brewing Company"])
    def test_search_breweries_by_name(self, name):
        response = requests.get(f'{BASE_URL}?by_name={name}')
        assert response.status_code == 200, 'false request'
        assert response.json()[0]['name'] == name

    @pytest.mark.parametrize('name', ['West'])
    def test_search_breweries_by_name(self, name):
        response = requests.get(f'{BASE_URL}?by_name={name}')
        assert response.status_code == 200, 'false request'
        assert 'West' in response.json()[0]['name']
        assert len(response.json()) == 20

    @pytest.mark.parametrize('city', ['Gilbert', 'Mesa', "Williamsville"])
    def test_search_breweries_by_city(self, city):
        response = requests.get(f'{BASE_URL}?by_city={city}')
        assert response.status_code == 200, 'false request'
        assert response.json()[0]['city'] == city

    @pytest.mark.parametrize('count', range(1, 51))
    def test_count_per_page(self, count):
        response = requests.get(f'{BASE_URL}?per_page={count}')
        print(response.json())
        assert len(response.json()) == count

    @pytest.mark.parametrize('count', (52, 53))
    def test_count_per_page(self, count):
        response = requests.get(f'{BASE_URL}?per_page={count}')
        print(response.status_code)
        print(response.json())
        assert len(response.json()) == 50

    @pytest.mark.parametrize('type', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor', 'closed'])
    def test_search_breweries_by_type(self, type: str):
        '''
        :param type: str
        При проверке не найденно ни одного значения при переменной 'proprietor'
        Проверка первого элемента из по типу пивоварни, из всего возращенного массива
        '''
        response = requests.get(f'{BASE_URL}?by_type={type}')
        assert response.status_code == 200, 'false request'
        assert response.json()[0]['brewery_type'] == type
