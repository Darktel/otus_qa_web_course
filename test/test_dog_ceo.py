import pytest
import requests
import cerberus

BASE_URL = 'https://dog.ceo/api/'
API_ALL = 'breeds/list/all'
API_RANDOM = 'breeds/image/random'
API_MULTIPLE_COLLECTION = ''


class Test_doc_ceo():

    def test_get_all_dog_list(self):
        response = requests.get(url=f'{BASE_URL}{API_ALL}')
        assert response.status_code == 200
        assert len(response.json()['message']) == 95

    def test_check_schema_all_dog_list(self):
        schema = {
            "message": {"type": "dict"},
            "status": {"type": "string"}
        }

        response = requests.get(url=f'{BASE_URL}{API_ALL}')
        v = cerberus.Validator(schema)
        assert v.validate(response.json())

    def test_get_random_dog(self):
        response = requests.get(url=f'{BASE_URL}{API_RANDOM}')
        assert response.status_code == 200

    def test_check_schema_random_dog(self):
        schema = {
            "message": {"type": "string"},
            "status": {"type": "string"}
        }

        response = requests.get(url=f'{BASE_URL}{API_RANDOM}')
        v = cerberus.Validator(schema)
        assert v.validate(response.json())

    @pytest.mark.parametrize('count_image', range(1, 3))
    @pytest.mark.parametrize('breed', ["hound", "mountain", "mastiff", "retriever"])
    def test_get_random_dog(self, count_image, breed):
        response = requests.get(url=f'{BASE_URL}breed/{breed}/images/random/{count_image}')
        assert response.status_code == 200
        # проверка кол-во возвращенных изображений соответствует переменной count_image
        assert len(response.json()['message']) == count_image
        # Проверка что в каждой ссылке на изображение присутствует заданная порода
        for __i in range(0, len(response.json()['message'])):
            assert breed in (response.json()['message'][__i])

    @pytest.mark.parametrize('breed', ["hound", "mountain", "mastiff", "retriever"])
    def test_get_sub_breed(self, breed):
        response = requests.get(url=f'{BASE_URL}breed/{breed}/list')
        assert response.status_code == 200
        assert len(response.text[0]) != 0
        schema = {
            "message": {"type": "string"},
            "status": {"type": "string"}
        }
        response = requests.get(url=f'{BASE_URL}{API_RANDOM}')
        v = cerberus.Validator(schema)
        assert v.validate(response.json())
