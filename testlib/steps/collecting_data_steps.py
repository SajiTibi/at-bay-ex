from testlib.api.age_api import age_api
from testlib.api.gender_api import gender_api
from testlib.api.nationality_api import nationality_api


class CollectDataSteps:

    @staticmethod
    def get_age(name):
        return age_api.get_age(name).json().get('age')

    @staticmethod
    def get_nationality(name):
        countries = nationality_api.get_nationalities(name).json().get('country')
        if not countries:
            return None

        return countries[0].get('country_id')

    @staticmethod
    def get_gender(name):
        return gender_api.get_gender(name).json().get('gender')


collect_data_steps = CollectDataSteps
