

import random

LIST_SIZE = 10
RANDOM_UPPER_BOUND = 30

l = []
for x in range(0, LIST_SIZE):  # как то можно сократить всю эту громозскую конструкцию с 2-мя условиями и 2-мя подусловиями ?
    if x not in l:
        l.append(random.randint(0, RANDOM_UPPER_BOUND))
no_duplicates = []
for x in l:
    if x not in no_duplicates:
        no_duplicates.append(x)

print(f"List l = {l}")
print(f"List dup_free = {no_duplicates}")


# Вариант без рандомного ввода списка

# LIST_SIZE = [5, 6, 8, 5 , 1, 8, 5, 2, 3, 4, 10]
#
# no_duplicates = []
# for x in LIST_SIZE:
#     if x not in no_duplicates:
#         no_duplicates(x)
#
# print(dup_free)