import requests

import schemas
import services
from parsers import hh_api_parser


def get_hh_vacancies_by_languages(
        languages: list[str],
        search_params: dict
) -> dict:

    vacancies_by_languages = {}

    for language in languages:
        vacancies = get_hh_vacancies_by_name_with_pagination(
            language,
            search_params
        )

        vacancies_processed, average_salary = services.get_average_salary(
            vacancies
        )

        vacancies_by_languages[language] = {
            'vacancies_found': len(vacancies),
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }

    return vacancies_by_languages


def get_hh_vacancies_by_name_with_pagination(
        name: str,
        search_params: dict
) -> list[schemas.Vacancy]:

    page = 0
    pages_number = 1
    vacancies = []
    search_params['text'] = f'"{name}"'

    while page < pages_number:
        search_params['page'] = page
        url = 'https://api.hh.ru/vacancies'
        headers = {
            'User-Agent': 'TestDev/1.0 (Phantom2525@gmail.com)'
        }

        response = requests.get(url, headers=headers, params=search_params)
        response.raise_for_status()
        hh_api_response = response.json()

        pages_number = int(hh_api_response['pages'])
        for vacancy in hh_api_response['items']:
            vacancies.append(
                hh_api_parser.parse_hh_response_vacancy(
                    vacancy
                )
            )
        page += 1

    return vacancies
