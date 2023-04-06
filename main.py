import services
import os
from api.super_job_api import get_sj_vacancies_by_languages
from api.hh_api import get_hh_vacancies_by_languages
from dotenv import load_dotenv


def main():
    load_dotenv()
    sj_api_token = os.getenv('SUPER_JOBS_API_TOKEN')

    search_hh_params = {
        'industry': '7.540',
        'area': '1',
        'period': '30',
        'per_page': '100'
    }
    search_vacancies_sj_params = {
        'town': 4,
        'catalogues': 48,
        'count': 100
    }

    program_languages = [
        'TypeScript',
        'Swift',
        'Scala',
        'Go',
        'C',
        'C#',
        'C++',
        'PHP',
        'Ruby',
        'Python',
        'Java',
        'JavaScript'
    ]

    hh_vacancies = get_hh_vacancies_by_languages(
        program_languages,
        search_hh_params
    )

    sj_vacancies = get_sj_vacancies_by_languages(
        program_languages,
        sj_api_token,
        search_vacancies_sj_params
    )

    services.print_vacancies_with_average_salary_as_table(
        hh_vacancies,
        'HeadHunter Moscow'
    )

    services.print_vacancies_with_average_salary_as_table(
        sj_vacancies,
        'SuperJob Moscow'
    )


if __name__ == '__main__':
    main()
