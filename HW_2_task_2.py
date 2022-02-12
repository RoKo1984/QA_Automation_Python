# Пользователь вводит трехзначное число. Найдите сумму его цифр.
# (используйте %)


your_number = int(input("Введите трехзначное число для определения суммы его чисел:")) # сумма числа будет "number_1+number_2+number_3"

number_3 = your_number % 10
number_2 = your_number % 100 // 10
number_1 = your_number // 100

total_number = number_1 + number_2 + number_3

common_number = ('Сумма цифр введенного числа: {}'.format(total_number))
print(common_number)

