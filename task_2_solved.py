# Дана история поисковых запросов: каждая строка — один введённый запрос.
# Повтор в списке значит, что этот запрос ввели ещё раз.
#
# Нужно найти:
#
# - сколько всего поисковых запросов в ленте
# - сколько раз ввели каждый запрос
# - какой запрос вводили чаще всего
# - какую долю всех поисков он занимает
# - какие запросы встретились один раз

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

counter = len(queries)
print(counter)
count_dict = {}
for query in queries:
    count_dict[query] = count_dict.get(query, 0) + 1
print(count_dict)
count_dict_max = max(count_dict, key=count_dict.get)
print(count_dict_max)
share_of_search = count_dict[count_dict_max] / sum(count_dict.values())
print(share_of_search)
for key, value in count_dict.items():
    if value == 1:
        print(key)
