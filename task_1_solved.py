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
print(moscow_kazan)
moscow_only = moscow - kazan
print(moscow_only)
kazan_only = kazan - moscow
print(kazan_only)
uniqque_products_count = len(moscow.union(kazan))
print(uniqque_products_count)
