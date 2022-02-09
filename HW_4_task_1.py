# Напишите программу для преобразования списка в кортеж

import random
list_size = 5
rate_use_random = 10
list_1 = []
for x in range(0, list_size):
    list_1.append(random.randint(0, rate_use_random))
print(f'list_1 = {list_1}')
print(type(list_1))

tuple_1 = tuple(list_1)
print(f'tuple_1 = {tuple_1}')
print(type(tuple_1))




