# import names
# import pytest as pytest
#
# from entities.person import Person
# from testlib.steps.collecting_data_steps import collect_data_steps
#
#
# @pytest.fixture(scope='session',autouse=False)
# def generate_names():
#     count = 5  # todo
#     res = []
#     for i in range(count):
#         name = names.get_first_name()
#         age = collect_data_steps.get_age(name)
#         nationality = collect_data_steps.get_nationality(name)
#         gender = collect_data_steps.get_gender(name)
#         res.append(Person(name, age, gender, nationality))
#
#     return res


# another approach of creating 5 data samples each session
