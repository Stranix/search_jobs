import schemas


def parse_hh_response_industry_area_specialization(industry_area: dict) -> list[schemas.Specialization]:
    specializations = []

    for specialization in industry_area['industries']:
        specializations.append(schemas.Specialization(specialization['id'], specialization['name']))

    return specializations


def parse_hh_response_industry(industry_area: dict) -> schemas.CompanyIndustry:
    specializations = parse_hh_response_industry_area_specialization(industry_area)

    return schemas.CompanyIndustry(industry_area['id'], industry_area['name'], specializations)


def parse_hh_response_vacancy_salary(vacancy: dict) -> schemas.Salary | None:
    if vacancy['salary']:
        return schemas.Salary(s_from=vacancy['salary']['from'],
                              to=vacancy['salary']['to'],
                              currency=vacancy['salary']['currency'],
                              gross=vacancy['salary']['gross']
                              )


def parse_hh_response_vacancy(vacancy: dict) -> schemas.Vacancy:
    return schemas.Vacancy(id=vacancy['id'],
                           name=vacancy['name'],
                           salary=parse_hh_response_vacancy_salary(vacancy),
                           url=vacancy['alternate_url'],
                           employer=vacancy['employer']['name'],
                           requirement=vacancy['snippet']['requirement'],
                           responsibility=vacancy['snippet']['responsibility']
                           )
