"""Фильтрация, группировка и агрегация плоских словарей."""

from collections import defaultdict


def filter_records(records, conditions=None, predicate=None):
    """Фильтрует записи по значениям полей и/или пользовательскому условию."""
    conditions = conditions or {}
    return [
        record
        for record in records
        if all(record.get(key) == value for key, value in conditions.items())
        and (predicate is None or predicate(record))
    ]


def group_by_attributes(records, attributes):
    """Группирует записи по атрибутам, используя кортежи в качестве ключей."""
    groups = defaultdict(list)
    for record in records:
        key = tuple(record.get(attribute) for attribute in attributes)
        groups[key].append(record)
    return dict(groups)


def aggregate_groups(records, attributes, aggregations):
    """Применяет именованные агрегирующие функции к каждой группе записей."""
    result = {}
    for group_key, group in group_by_attributes(records, attributes).items():
        result[group_key] = {
            name: aggregation(group)
            for name, aggregation in aggregations.items()
        }
    return result
