# Есть список отзывов на товары. На каждой строке — по одному. Данные
# слегка битые, и названия товара записаны в разном регистре. `id` при
# этом один и тот же для одного и того же товара. Перед подсчётом
# приведите названия к одному формату, иначе они будут считаться как
# разные`.
#
# Нужно найти:
#
# - среднюю оценку каждого товара
# - худший товар по средней оценке среди тех, у кого хотя бы два отзыва
# - сколько отзывов на 1 или 2 звезды
# - какую долю всех отзывов они составляют

from collections import defaultdict

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

reviews_corrected = [
    {**item, "product": item["product"].lower()}
    for item in reviews
]
# print(reviews_corrected)
avg_mark_by_product = {
    item["product"]: sum(
        review["stars"]
        for review in reviews_corrected
        if review["product"] == item["product"]
    )
    / len(
        [
            review
            for review in reviews_corrected
            if review["product"] == item["product"]
        ]
    )
    for item in reviews_corrected
}

groups = defaultdict(lambda: {"count": 0, "stars_sum": 0})

for review in reviews_corrected:
    product = review["product"]
    groups[product]["count"] += 1
    groups[product]["stars_sum"] += review["stars"]

result = {
    product: {
        "count": data["count"],
        "average": data["stars_sum"] / data["count"],
    }
    for product, data in groups.items()
    if data["count"] > 1
}

product_with_min_average = min(
    result,
    key=lambda x: result[x]["average"],
)
reviews_number = len(reviews_corrected)
reviews_1_2_count = sum(
    1 for review in reviews_corrected if review["stars"] in [1, 2]
)
bad_reviews_share = reviews_1_2_count / reviews_number
print(f"Средние оценки по товарам: {avg_mark_by_product}")
print(f"Худший товар по средней оценке: {product_with_min_average}")
print(f"Всего отзывов: {reviews_number}")
print(f"Количество отзывов на 1 или 2 звезды: {reviews_1_2_count}")
print(f"Доля отзывов на 1 или 2 звезды: {bad_reviews_share:.1%}")
