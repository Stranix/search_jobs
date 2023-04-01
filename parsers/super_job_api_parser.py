import schemas


def parse_sj_response_industry_area_specialization(industry_area: dict) -> list[schemas.Specialization]:
    specializations = []

    for specialization in industry_area['positions']:
        specializations.append(schemas.Specialization(specialization['key'], specialization['title']))

    return specializations


def parse_sj_response_industry(industry_area: dict) -> schemas.CompanyIndustry:
    specializations = parse_sj_response_industry_area_specialization(industry_area)

    return schemas.CompanyIndustry(industry_area['key'], industry_area['title'], specializations)


def parse_sj_response_vacancy_salary(vacancy: dict) -> schemas.Salary | None:
    if vacancy['payment_from'] or vacancy['payment_to']:
        return schemas.Salary(s_from=vacancy['payment_from'],
                              to=vacancy['payment_to'],
                              currency=vacancy['currency'],
                              gross=False
                              )


def parse_sj_response_vacancy(vacancy: dict) -> schemas.Vacancy:
    return schemas.Vacancy(id=vacancy['id'],
                           name=vacancy['profession'],
                           salary=parse_sj_response_vacancy_salary(vacancy),
                           url=vacancy['link'],
                           employer=vacancy['client'].get('title', ''),
                           requirement=vacancy['candidat'],
                           responsibility=vacancy['candidat']
                           )
