# Напишите программу, чтобы проверить, не имеют ли два
# заданных набора (set) общих элементов.

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

print(f'Множество a = {a}')
print(f'Множество b = {b}')

z = a & b
print(f'Общий элемент в двух множествах: {z}')




