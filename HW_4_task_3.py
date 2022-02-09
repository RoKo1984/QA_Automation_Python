# Напишите программу для поэлементного вычисления суммы
# заданных кортежей. Результатом должен быть кортеж.
# Input
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Output
# (6, 9, 8, 6)

# Решение
tuple_1 = (1, 2, 3, 4)
tuple_2 = (3, 5, 2, 1)
tuple_3 = (2, 2, 3, 1)

a = list(tuple_1)
b = list(tuple_2)
c = list(tuple_3)

print(type(a), a)
print(type(b), b)
print(type(c), c)


sum = [0]*len(a)
for indx in [a, b, c]:
    for i in range(len(indx)):
        sum[i] += indx[i]
sum = tuple(sum)
print(f'сумма значений =  {sum}')
print(type(sum))


