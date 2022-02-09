# Реализовать логику Difference для двух списков (list), проверить работу
# алгоритма на set.difference

l1 = [10, 20, 30, 40, 50]
l3 = [50, 75, 30, 20, 40, 69]


import random

LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10


a = []
b = []
for _ in range(0, LIST_SIZE):
    a.append(random.randint(0, RANDOM_UPPER_BOUND))
    b.append(random.randint(0, RANDOM_UPPER_BOUND))

print(f'список a = {a}')
print(f'список b = {b}')

res = []
c = []
for x in a:
    if x not in b:
        res.append(x)
        for item in res:
            if item not in c:
                c.append(item)
print()
print(f'Результат = {c}') # вариант 1
print()
# print(f'Результат = {list(set(res))}') # вариант записи для того чтобы исключить повторяющиеся цифры в списке. Только нужно закоментировать строки 28 - 30
print()

a = set(a)
b = set(b)
z = a.difference(b)
print(f'Проверка по алгоритму  на set.difference: {z}')
