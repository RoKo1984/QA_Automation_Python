number_1 = int(input("Введите 1-е любое целое число:\t"))
number_2 = int(input("Введите 2-е любое целое число:\t"))
number_3 = int(input("Введите 3-е любое целое число:\t"))

if number_1 >= number_2 and number_1 >= number_3:
    result_1 = f'максимальное число из трех введенных: {number_1}'
    print(result_1)

elif number_1 <= number_2 and number_2 >= number_3:
    result_2 = f'максимальное число из трех введенных: {number_2}'
    print(result_2)

elif number_1 <= number_3 and number_2 <= number_3:
    result_3 = f'максимальное число из трех введенных: {number_3}'
    print(result_3)

elif number_1 == number_2 and number_2 == number_3:        # не разобрался пока, как вывести только это условие, когда все числа одинаковые и не выводить никакое число
    print("Обратите внимание, Вы ввели одинаковые числа")

