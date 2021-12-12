import pytest
import requests
import cerberus

BASE_URL = 'https://jsonplaceholder.typicode.com/posts/'


class Test_doc_ceo():

    @pytest.mark.parametrize('ID_POST', (1, 2, 3))
    def test_get_post(self, ID_POST):
        response = requests.get(url=f'{BASE_URL}{ID_POST}')
        assert response.status_code == 200

    @pytest.mark.parametrize('ID_POST', (1, 2, 3))
    def test_check_schema_post(self, ID_POST):
        schema = {
            "body": {"type": "string"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "userId": {"type": "integer"}
        }

        response = requests.get(url=f'{BASE_URL}{ID_POST}')
        v = cerberus.Validator(schema)
        assert v.validate(response.json())

    def test_create_post(self):
        data_post = {
            "title": 'title post',
            "body": 'The issue of randomness is an important philosophical and theoretical question.',
            "userId": 2
        }

        response = requests.post(url=BASE_URL, json=data_post)
        assert response.json()['id'] == 101
        assert response.json()['userId'] == 2
        assert response.json()['title'] == 'title post'
        assert 'important philosophical' in response.json()['body']

    def test_updating_post(self):
        data_post = {
            "id": 1,
            "title": 'foo',
            "body": 'bar',
            "userId": 1
        }

        schema = {
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"},
            "userId": {"type": "integer"}
        }

        response = requests.put(url=f'{BASE_URL}1', json=data_post)
        v = cerberus.Validator(schema)
        assert v.validate(response.json())
        assert response.json()['body'] == 'bar'

    @pytest.mark.parametrize('users', (2, 4, 5, 1))
    def test_filter_post(self, users):
        response = requests.get(url=f'{BASE_URL}?userId={users}')
        assert int(response.json()[0]['userId']) == users
        assert response.json() is not None
