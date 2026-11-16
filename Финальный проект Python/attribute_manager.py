"""Вспомогательные функции для добавления и удаления атрибутов словарей."""


class AttributeManager:
    """Применяет заданные преобразования к плоским словарям записей."""

    def __init__(self, transformations=None):
        """Сохраняет преобразования, применяемые при добавлении атрибутов."""
        self.transformations = transformations or {}

    def add_attributes(self, records):
        """Возвращает копии записей с добавленными атрибутами."""
        enriched = []
        for record in records:
            updated = dict(record)
            for name, transformation in self.transformations.items():
                updated[name] = transformation(record)
            enriched.append(updated)
        return enriched

    @staticmethod
    def remove_attributes(records, attributes):
        """Возвращает копии записей без выбранных атрибутов."""
        excluded = set(attributes)
        return [
            {
                key: value
                for key, value in record.items()
                if key not in excluded
            }
            for record in records
        ]
