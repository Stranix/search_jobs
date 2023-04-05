import schemas


def parse_hh_response_vacancy_salary(vacancy: dict) -> schemas.Salary | None:
    if vacancy['salary']:
        return schemas.Salary(
            s_from=vacancy['salary']['from'],
            to=vacancy['salary']['to'],
            currency=vacancy['salary']['currency'],
            gross=vacancy['salary']['gross']
        )


def parse_hh_response_vacancy(vacancy: dict) -> schemas.Vacancy:
    return schemas.Vacancy(
        id=vacancy['id'],
        name=vacancy['name'],
        salary=parse_hh_response_vacancy_salary(vacancy),
    )
