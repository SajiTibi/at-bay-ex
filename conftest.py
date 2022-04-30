import names

from entities.person import Person
from testlib.steps.collecting_data_steps import collect_data_steps


# pytest_plugins = [
#     'testlib.fixtures.create_names_fixtures'
# ]
# related to : another approach of creating 5 data samples each session


def generate_names():
    count = 5
    res = []
    for i in range(count):
        # TODO: need to do more verification on the data, some properties might return None so a retry logic
        # is needed to make sure we have 5 valid persons
        name = names.get_first_name()
        age = collect_data_steps.get_age(name)
        nationality = collect_data_steps.get_nationality(name)
        gender = collect_data_steps.get_gender(name)
        p = Person(name, age, gender, nationality)
        res.append(p)

    return res


def pytest_generate_tests(metafunc):
    if 'test_input' not in metafunc.fixturenames:
        return

    test_cases = generate_names()

    if not test_cases:
        raise ValueError("Test cases not loaded")

    return metafunc.parametrize("test_input", test_cases)
