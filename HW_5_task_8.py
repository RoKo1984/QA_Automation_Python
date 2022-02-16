# Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном случае. 8
# - YES, 3 - NO


def degree_function_num(n):
    if n % 2 != 0:
        return print('NO')
    else:
        if n == 2:
            return print('YES')
        else:
            degree_function_num(n / 2)

degree_function_num(16)
