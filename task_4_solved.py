# Есть статистика за пять дней работы магазина. У каждого дня число
# заказов, выручка и число возвратов.
#
# Нужно найти:
#
# - выручку за всю неделю
# - день с самой большой выручкой
# - среднюю выручку на один заказ в каждый день
# - дни, где возвратов больше 20% заказов

days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]
revenue_sum = sum(item.get("revenue", 0) for item in days)
day_with_max_revenue = max(
    days,
    key=lambda x: x.get("revenue", 0),
)
average_revenue_by_day = revenue_sum / len(days)

average_revenue_by_day = {
    item["day"]: item["revenue"] / item["orders"]
    for item in days
}
days_with_many_returns = {
    item["day"]: item["returns"] / item["orders"]
    for item in days
    if item["returns"] / item["orders"] > 0.2
}

print(f"Дни, когда возвратов больше 20%: {days_with_many_returns}")
print(f"Средняя выручка на заказ по дням: {average_revenue_by_day}")
print(f"Общая выручка за неделю: {revenue_sum}")
print(f"День с самой большой выручкой: {day_with_max_revenue['day']}")
