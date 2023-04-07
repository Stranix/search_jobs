import schemas


def parse_sj_response_vacancy(vacancy: dict) -> schemas.Vacancy:
    salary = None

    if vacancy['payment_from'] or vacancy['payment_to']:
        salary = schemas.Salary(
            s_from=vacancy['payment_from'],
            to=vacancy['payment_to'],
            currency=vacancy['currency'],
            gross=False
        )

    vacancy = schemas.Vacancy(
        id=vacancy['id'],
        name=vacancy['profession'],
        salary=salary,
    )

    return vacancy
