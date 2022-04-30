import requests as requests


class BaseApi:
    api_url = ''
    session = requests.session()

    headers = {
        "accept": "application/json",
    }

    @classmethod
    def api_get(cls, params=None, **kwargs):
        return cls.session.get(f'{cls.api_url}', headers=cls.headers, params=params, **kwargs)
