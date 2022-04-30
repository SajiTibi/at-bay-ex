from testlib.api.helpers_api import BaseApi


class GenderApi(BaseApi):
    api_url = 'https://api.genderize.io/'

    @staticmethod
    def get_gender(name):
        return GenderApi.api_get(params={'name': name})


gender_api = GenderApi
