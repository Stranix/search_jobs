import schemas


def parse_sj_response_vacancy_salary(vacancy: dict) -> schemas.Salary | None:
    if vacancy['payment_from'] or vacancy['payment_to']:
        return schemas.Salary(
            s_from=vacancy['payment_from'],
            to=vacancy['payment_to'],
            currency=vacancy['currency'],
            gross=False
        )


def parse_sj_response_vacancy(vacancy: dict) -> schemas.Vacancy:
    return schemas.Vacancy(
        id=vacancy['id'],
        name=vacancy['profession'],
        salary=parse_sj_response_vacancy_salary(vacancy),
    )
