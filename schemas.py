from dataclasses import dataclass


@dataclass
class Specialization:
    id: str
    name: str


@dataclass
class CompanyIndustry:
    id: str
    name: str
    specializations: list[Specialization]


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
    url: str
    employer: str
    requirement: str
    responsibility: str
