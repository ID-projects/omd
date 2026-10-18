# Есть список заказов:
# - `status` -  статус заказа
#   - `delivered` доставлен покупателю
#   - `returned` возврат
# - `amount` — сумма заказа.
#
# Нужно найти:
#
# - на какую сумму оформили возвраты
# - кто хотя бы раз вернул заказ
# - сколько заказов доставлено покупателю
# - средний чек доставленных заказов

orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

returned_sum = sum(
    order["amount"]
    for order in orders
    if order["status"] == "returned"
)
print(f"Сумма возвратов: {returned_sum}")

returners_list = [
    order["buyer"]
    for order in orders
    if order["status"] == "returned"
]
print(f"Покупатели, вернувшие заказ: {returners_list}")
returned_count = len(returners_list)
print(f"Количество возвращённых заказов: {returned_count}")

delivered_count = sum(
    1 for order in orders if order["status"] == "delivered"
)
print(f"Количество доставленных заказов: {delivered_count}")
delivered_sum = sum(
    order["amount"]
    for order in orders
    if order["status"] == "delivered"
)
print(f"Сумма доставленных заказов: {delivered_sum}")
avg_delivered_sum = delivered_sum / delivered_count
print(f"Средний чек доставленного заказа: {avg_delivered_sum}")
