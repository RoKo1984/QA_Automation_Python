# Напишите программу для поиска элементов в данном наборе A
# (set), которых нет в другом наборе B.

import random

LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10


a = []
b = []
for _ in range(0, LIST_SIZE):
    a.append(random.randint(0, RANDOM_UPPER_BOUND))
    b.append(random.randint(0, RANDOM_UPPER_BOUND))

a = set(a)
b = set(b)
z = a.difference(b)


print(f'Множество a = {a}')
print(f'Множество a = {b}')


print(f'Уникальные элементы set(a), которых нет в set(b): {z}')