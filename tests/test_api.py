import requests
import pytest

@pytest.mark.api
def test_healthchecks_api():
    headers = {'Content-Type': 'application/json'}
    url = 'http://10.243.5.2/apps/'
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200
