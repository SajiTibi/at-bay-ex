from testlib.steps.assertion_steps.data_assertion_steps import data_assertion_steps
from testlib.steps.collecting_data_steps import collect_data_steps


def test_names(test_input):
    person_name = test_input.name
    age = collect_data_steps.get_age(person_name)
    gender = collect_data_steps.get_gender(person_name)
    nationality = collect_data_steps.get_nationality(person_name)

    data_assertion_steps.check_age(test_input, age)
    data_assertion_steps.check_gender(test_input, gender)
    data_assertion_steps.check_nationality(test_input, nationality)
