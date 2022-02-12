# Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном случае. 8
# - YES, 3 - NO

a = int(input())
n = 2
while a != n and a >= n:
n = n * 2
if a == n:
print('YES')
else:
print('NO')