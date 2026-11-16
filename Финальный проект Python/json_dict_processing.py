"""Функции для извлечения и преобразования вложенных JSON-словарей."""

from collections.abc import Mapping


def extract_nested_value(obj, keys):
    """Извлекает значение по цепочке ключей или возвращает None
    при отсутствии пути.
    """
    value = obj
    for key in keys:
        if not isinstance(value, Mapping) or key not in value:
            return None
        value = value[key]
    return value


def process_dictionary_with_config(dictionary, config):
    """Преобразует словарь в плоский согласно конфигурации путей
    и обработчиков.
    """
    result = {}
    for attribute, definition in config.items():
        if (
            isinstance(definition, tuple)
            and len(definition) == 2
            and callable(definition[1])
        ):
            path, processor = definition
            value = extract_nested_value(dictionary, path)
            result[attribute] = processor(value)
        else:
            result[attribute] = extract_nested_value(dictionary, definition)
    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    """Обрабатывает каждый словарь в списке по заданной конфигурации."""
    if list_of_dicts is None:
        return []
    return [
        process_dictionary_with_config(dictionary, config)
        for dictionary in list_of_dicts
    ]


def create_processor(config, list_processor=False):
    """Создаёт процессор с заданной конфигурацией для словаря или списка."""
    if list_processor:
        return lambda dictionaries: process_list_of_dicts_with_config(
            dictionaries, config
        )
    return lambda dictionary: process_dictionary_with_config(
        dictionary, config
    )
