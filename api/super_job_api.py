import requests
import schemas
import services
from parsers import super_job_api_parser


def get_sj_vacancies_by_name_with_pagination(
        name: str,
        api_token: str,
        search_params: dict
) -> list[schemas.Vacancy]:
    page = 0
    vacancies = []

    search_params.update(
        keyword=name,
        profession_only=1
    )

    while True:
        search_params['page'] = page
        url = 'https://api.superjob.ru/2.20/vacancies'
        headers = {
            'User-Agent': 'TestDev/1.0 (Phantom2525@gmail.com)',
            'X-Api-App-Id': api_token
        }

        response = requests.get(url, headers=headers, params=search_params)
        response.raise_for_status()
        sj_api_response = response.json()

        for vacancy in sj_api_response['objects']:
            vacancies.append(
                super_job_api_parser.parse_sj_response_vacancy(
                    vacancy
                )
            )
        if not sj_api_response['more']:
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
        vacancies = get_sj_vacancies_by_name_with_pagination(
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
