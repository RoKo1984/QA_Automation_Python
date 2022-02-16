# Дано натуральное число N. Вычислите сумму его цифр.
# Напишите рекурсивную функцию

def sum_numbers(n):
    if n == 0:
        return 0
    return n % 10 + sum_numbers(n//10)
print(sum_numbers(123))




