import requests


def test_status(url, status_code):
    response = requests.get(url)
    print(response.status_code)
    assert response.status_code == int(status_code)
