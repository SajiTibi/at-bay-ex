from hamcrest import assert_that


class DataAssertionSteps:

    @staticmethod
    def check_age(person, expected):
        assert_that(person.age, expected, f'Got age: {person.age} instead of {expected}')

    @staticmethod
    def check_gender(person, expected):
        assert_that(person.gender, expected, f'Got gender: {person.gender} instead of {expected}')

    @staticmethod
    def check_nationality(person, expected):
        assert_that(person.nationality, expected, f'Got nationality: {person.nationality} instead of {expected}')


data_assertion_steps = DataAssertionSteps
