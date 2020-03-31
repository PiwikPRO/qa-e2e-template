import requests


class Api():
    def __init__(self, context):
        context.browser

    def get_apps(self):
        headers = {'Content-Type': 'application/json'}
        url = 'http://10.243.5.2/apps/'
        response = requests.get(url=url, headers=headers)
        assert response.status_code == 200
