# Даны два целых числа A и В. Выведите все числа от A до B включительно,
# в порядке возрастания, если A < B, или в порядке убывания если A > B

print('Введите два любых целых числа a и b')
a = int(input("a = "))
b = int(input("b = "))

if a <= b:
    for idx in range(a, b + 1):
        print(idx, end=" ")
else:
    for idx in range(a, b - 1, -1):
        print(idx, end=" ")