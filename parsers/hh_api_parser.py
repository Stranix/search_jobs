import schemas


def parse_hh_response_vacancy(vacancy: dict) -> schemas.Vacancy:
    salary = None

    if vacancy['salary']:
        salary = schemas.Salary(
            s_from=vacancy['salary']['from'],
            to=vacancy['salary']['to'],
            currency=vacancy['salary']['currency'],
            gross=vacancy['salary']['gross']
        )

    vacancy = schemas.Vacancy(
        id=vacancy['id'],
        name=vacancy['name'],
        salary=salary,
    )

    return vacancy
