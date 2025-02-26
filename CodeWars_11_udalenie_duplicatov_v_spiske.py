#удаление дубликатов и рандомная сортировка
#def distinct(seq):
 #   return list(set(seq))


#можно так
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique_lst = []
# seen = set()
#
# for item in lst:
#     if item not in seen:
#         unique_lst.append(item)
#         seen.add(item)
#
# print(unique_lst)  # Выведет: [1, 2, 3, 4, 5]

#и вот так
#сортед - типо отсортируй по ключу, который является индексами оригинального списка
#def distinct(seq):
 #   return sorted(set(seq), key = seq.index)

#топовое решение
def distinct(seq):
    return list(dict.fromkeys(seq))



