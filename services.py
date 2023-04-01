import requests
import schemas
from terminaltables import AsciiTable


def send_request_to_hh_api(point: str, params: dict = None) -> dict:
    url = f'https://api.hh.ru/{point}'
    headers = {
        'User-Agent': 'TestDev/1.0 (Phantom2525@gmail.com)'
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()


def send_request_to_sj_api(api_token: str, point: str, params: dict = None) -> dict:
    url = f'https://api.superjob.ru/2.20/{point}'
    headers = {
        'User-Agent': 'TestDev/1.0 (Phantom2525@gmail.com)',
        'X-Api-App-Id': api_token
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()


def get_average_salary(vacancies: list[schemas.Vacancy], currency: str = 'RUR') -> tuple[int, float]:
    salaries = []

    for vacancy in vacancies:
        if not vacancy.salary or vacancy.salary.currency != currency:
            continue
        salaries.append(predict_salary(vacancy))

    average_salary = 0.0
    vacancies_processed = len(salaries)

    if salaries:
        average_salary = sum(salaries) // len(salaries)

    return vacancies_processed, average_salary


def predict_salary(vacancy: schemas.Vacancy) -> float:
    if vacancy.salary.s_from is None:
        return float(vacancy.salary.to * 0.8)

    if vacancy.salary.to is None:
        return float(vacancy.salary.s_from * 1.2)

    return float((vacancy.salary.s_from + vacancy.salary.to) / 2)


def print_language_table(language_data: dict, table_name: str):
    headers = ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    table_data = [headers]

    for language, stats in language_data.items():
        line = [language, stats['vacancies_found'], stats['vacancies_processed'], stats['average_salary']]
        table_data.append(line)

    table_instance = AsciiTable(table_data, table_name)

    print(table_instance.table, end='\n\n')
