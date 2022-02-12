# Напишите рекурсивную функцию для вычисления числа Фибоначи

n = int(input("Введите любое целое число для определения числа Фибоначи: "))
def fibonachi(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)
print(f'\nчисло Фибоначи от {n} = {fibonachi(n)}')

