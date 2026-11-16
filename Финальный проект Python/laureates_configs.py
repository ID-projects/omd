"""Конфигурации и процессоры для лауреатов-людей и организаций."""

from json_dict_processing import create_processor
from prizes_configs import prize_processor


def process_year(year_string):
    """Извлекает четырёхзначный год из строки даты."""
    if not year_string:
        return None
    year = str(year_string)[:4]
    return int(year) if year.isdigit() else None


CONFIG_PERSON = {
    "id": (["id"], lambda value: int(value) if value is not None else None),
    "name": ["knownName", "en"],
    "gender": ["gender"],
    "birth_year": (["birth", "date"], process_year),
    "country_birth": ["birth", "place", "country", "en"],
    "country_now": ["birth", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor()),
}

CONFIG_ORG = {
    "id": (["id"], lambda value: int(value) if value is not None else None),
    "name": ["orgName", "en"],
    "founded_year": (["founded", "date"], process_year),
    "country_founded": ["founded", "place", "country", "en"],
    "country_now": ["founded", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor()),
}


def person_processor():
    """Создаёт процессор для записи о лауреате-человеке."""
    return create_processor(CONFIG_PERSON)


def org_processor():
    """Создаёт процессор для записи о лауреате-организации."""
    return create_processor(CONFIG_ORG)


def process_persons(people):
    """Обрабатывает список лауреатов-людей."""
    processor = person_processor()
    return [processor(person) for person in people]


def process_orgs(organizations):
    """Обрабатывает список лауреатов-организаций."""
    processor = org_processor()
    return [processor(organization) for organization in organizations]


assert process_year("2001-10-10") == 2001
assert process_year("1917-00-00") == 1917
