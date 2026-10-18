# Один и тот же товар может лежать на складе в Москве, в Казани или в
# обоих городах. Ниже id товаров на каждом складе.
#
# Нужно найти:
#
# - что можно забрать в любом из двух городов
# - что есть только в Москве
# - что есть только в Казани
# - сколько разных товаров на обоих складах вместе

moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

moscow_kazan = moscow & kazan
print(f"Товары, доступные в обоих городах: {sorted(moscow_kazan)}")
moscow_only = moscow - kazan
print(f"Товары, доступные только в Москве: {sorted(moscow_only)}")
kazan_only = kazan - moscow
print(f"Товары, доступные только в Казани: {sorted(kazan_only)}")
uniqque_products_count = len(moscow.union(kazan))
print(f"Всего разных товаров на двух складах: {uniqque_products_count}")
