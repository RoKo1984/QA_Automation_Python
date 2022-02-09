# Напишите программу, которая удаляет пересечение 2-го набора
# из 1-го набора.

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
z = a.union(b)

print(f'Множество a = {a}')
print(f'Множество a = {b}')


print(f'Уникальные элементы в двух множеств set(a) и set(b): {z}')
