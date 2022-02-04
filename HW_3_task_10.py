
dic1 = dict()
for x in range(1, 16):
    dic1[x] = x**2

print(dic1)

# Вариант записи №2
dic1 = {a: a ** 2 for a in range(1, 16)}
print(dic1)