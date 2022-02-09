# Реализовать логику Union для двух списков (list), проверить работу
# алгоритма на set.union

import random

LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10


a = []
b = []
for _ in range(0, LIST_SIZE):
    a.append(random.randint(0, RANDOM_UPPER_BOUND))
    b.append(random.randint(0, RANDOM_UPPER_BOUND))

print(f'список a:  {a}')
print(f'список b:  {b}')

g = []
for i in a + b:
    if not i in g:
        g.append(i)
print()
print(f'Результат уникальных данных:  {g}')
print()

# Проверка по set.union
a = set(a)
b = set(b)
z = a.union(b)

print(f'Проверка по алгоритму  на set.union: {z}')