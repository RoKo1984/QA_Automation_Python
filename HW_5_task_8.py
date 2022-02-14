# Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном случае. 8
# - YES, 3 - NO


def f(n):
    if n % 2 != 0:
        return print('NO')
    else:
        if n == 2:
            return print('YES')
        else:
            f(n / 2)

f(16)
