
import random

LIST_SIZE = 3
RANDOM_UPPER_BOUND = 5

a = []
b = []
c = []
for x in range(0, LIST_SIZE):
    a.append(random.randint(0, RANDOM_UPPER_BOUND))
    b.append(random.randint(0, RANDOM_UPPER_BOUND))
for i in a:
    if i in b:
        continue
    else: c.append(i)
for j in b:
    if j in a:
        continue
    else: c.append(j)
    for j in b:
        if j != j:
            c.append(j)
            break


print(f"List a = {a}")
print(f"List b = {b}")
print(f"List c = {list(set(c))}")


