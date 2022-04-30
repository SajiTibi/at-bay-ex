from testlib.api.helpers_api import BaseApi


class AgeApi(BaseApi):
    api_url = 'https://api.agify.io/'

    @staticmethod
    def get_age(name):
        return AgeApi.api_get(params={'name': name})


age_api = AgeApi
