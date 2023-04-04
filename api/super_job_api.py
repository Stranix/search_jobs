import schemas
import services
from parsers import super_job_api_parser


def get_sj_vacancies_by_name_with_paginations(
        name: str,
        api_token: str,
        search_params: dict
) -> list[schemas.Vacancy]:
    page = 0
    vacancies = []

    search_params.update({
        'keywords': name,
        'profession_only': '1'
    })

    while True:
        search_params['page'] = page
        response_sj_api = services.send_request_to_sj_api(
            api_token,
            'vacancies',
            search_params
        )
        for vacancy in response_sj_api['objects']:
            vacancies.append(
                super_job_api_parser.parse_sj_response_vacancy(
                    vacancy
                )
            )
        if not response_sj_api['more']:
            break
        page += 1

    return vacancies


def get_sj_vacancies_by_languages(
        languages: list[str],
        api_token: str,
        search_params: dict
) -> dict:
    vacancies_by_languages = {}

    for language in languages:
        vacancies = get_sj_vacancies_by_name_with_paginations(
            language,
            api_token,
            search_params
        )
        vacancies_processed, average_salary = services.get_average_salary(
            vacancies,
            'rub'
        )

        vacancies_by_languages[language] = {
            'vacancies_found': len(vacancies),
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }

    return vacancies_by_languages
