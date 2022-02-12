# Напишите функцию Python для суммирования всех чисел в списке.

import random

LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10
list = []

for _ in range(0, LIST_SIZE):
    list.append(random.randint(0, RANDOM_UPPER_BOUND))

print(f'список:  {list}')

def sum(list):
    s = 0
    for i in list:
        s = s + i
    return print(f'сумма чисел списка равна: sum = {s}')

sum(list)



