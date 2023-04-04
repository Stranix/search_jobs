import schemas
import services
from parsers import hh_api_parser


def get_hh_industries() -> list[schemas.CompanyIndustry]:
    response_hh_api = services.send_request_to_hh_api('industries')

    industries = []
    for industry_area in response_hh_api:
        company_industry = hh_api_parser.parse_hh_response_industry(industry_area)
        industries.append(company_industry)

    return industries


def get_hh_industry_area_by_name(name: str) -> schemas.CompanyIndustry | None:
    industries = get_hh_industries()

    for industry_area in industries:
        if industry_area.name == name:
            return industry_area


def get_hh_specialization_by_name(name: str) -> schemas.Specialization | None:
    industries = get_hh_industries()

    for industry in industries:
        for specialization in industry.specializations:
            if specialization.name == name:
                return specialization


def get_hh_vacancies_by_languages(languages: list[str], search_params: dict) -> dict:
    vacancies_by_languages = {}

    for language in languages:
        vacancies = get_hh_vacancies_by_name_with_paginations(language, search_params)
        vacancies_processed, average_salary = services.get_average_salary(vacancies)

        vacancies_by_languages[language] = {
            'vacancies_found': len(vacancies),
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }

    return vacancies_by_languages


def get_hh_vacancies_by_name_with_paginations(name: str, search_params: dict) -> list[schemas.Vacancy]:
    page = 0
    pages_number = 1
    vacancies = []
    search_params.update({'text': f'"{name}"'})

    while page < pages_number:
        search_params.update({'page': page})
        response_hh_api = services.send_request_to_hh_api('vacancies', search_params)
        pages_number = int(response_hh_api['pages'])
        for vacancy in response_hh_api['items']:
            vacancies.append(hh_api_parser.parse_hh_response_vacancy(vacancy))
        page += 1

    return vacancies