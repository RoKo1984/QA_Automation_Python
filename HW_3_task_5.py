print('Введите два целых числа a и b при этом  a < b')
a = int(input("a = "))
b = int(input("b = "))

for idx in range(a, b + 1):
    print(idx, end=" ")

if a >= b:
    print('Вы не выполнили условие a < b')