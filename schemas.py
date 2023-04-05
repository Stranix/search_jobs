from dataclasses import dataclass


@dataclass
class Salary:
    s_from: float | None
    to: float | None
    currency: str
    gross: bool


@dataclass
class Vacancy:
    id: int
    name: str
    salary: Salary | None
