from testlib.api.helpers_api import BaseApi


class NationalityApi(BaseApi):
    api_url = 'https://api.nationalize.io/'

    @staticmethod
    def get_nationalities(name):
        return NationalityApi.api_get(params={'name': name})


nationality_api = NationalityApi
