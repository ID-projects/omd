"""Общие агрегирующие функции для коллекций плоских словарей."""

from statistics import mean, median


def values_for(records, metric):
    """Собирает непустые значения указанного показателя."""
    return [
        record[metric]
        for record in records
        if record.get(metric) is not None
    ]


def count(records):
    """Возвращает количество записей."""
    return len(records)


def count_unique(records, metric):
    """Считает количество уникальных непустых значений показателя."""
    return len(
        {
            record[metric]
            for record in records
            if record.get(metric) is not None
        }
    )


def average(records, metric):
    """Вычисляет среднее числового показателя или возвращает None
    для пустого набора.
    """
    values = values_for(records, metric)
    return mean(values) if values else None


def median_value(records, metric):
    """Вычисляет медиану показателя или возвращает None для пустого набора."""
    values = values_for(records, metric)
    return median(values) if values else None


def maximum(records, metric):
    """Возвращает максимум показателя или None для пустого набора."""
    values = values_for(records, metric)
    return max(values) if values else None


def top_n(records, metric, n=10, reverse=True):
    """Возвращает первые ``n`` записей, отсортированных по показателю."""
    if n < 0:
        raise ValueError("n must be non-negative")
    eligible = [record for record in records if record.get(metric) is not None]
    return sorted(
        eligible, key=lambda record: record[metric], reverse=reverse
    )[:n]
