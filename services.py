import schemas
from terminaltables import AsciiTable


def get_average_salary(
        vacancies: list[schemas.Vacancy],
        currency: str = 'RUR'
) -> tuple[int, float]:
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
    if not vacancy.salary.s_from:
        return float(vacancy.salary.to * 0.8)

    if not vacancy.salary.to:
        return float(vacancy.salary.s_from * 1.2)

    return float((vacancy.salary.s_from + vacancy.salary.to) / 2)


def print_vacancies_with_average_salary_as_table(
        vacancies_by_languages: dict,
        table_name: str
):

    headers = [
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
    ]
    table_row = [headers]

    for language, stats in vacancies_by_languages.items():
        line = [
            language,
            stats['vacancies_found'],
            stats['vacancies_processed'],
            stats['average_salary']
        ]
        table_row.append(line)

    table_instance = AsciiTable(table_row, table_name)

    print(table_instance.table, end='\n\n')
