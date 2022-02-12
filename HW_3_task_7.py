# Напишите программу, которая копирует список

import random

LIST_SIZE = 5
RANDOM_UPPER_BOUND = 10

l = []
l_copy = []
for x in range(0, LIST_SIZE):
    l.append(random.randint(0, RANDOM_UPPER_BOUND))

# Вариант 1
# l_copy = l.copy()

# Вариант 2
for g in l:
        l_copy.append(g)

print(f"List: {l}")
print(f"Copy_List: {l_copy}")




