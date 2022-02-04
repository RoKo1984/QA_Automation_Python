print('Дана функция y = f(x)')

x = float(input("Введите значение x = "))

if x > 0:
    y = 2*x - 10
    result_1 = f'y= : {y}'
    print(result_1)
elif x == 0:
    y = 0
    result_2 = f'y= : {y}'
    print(result_2)
elif x < 0:
    y = 2*x*(-1) - 1  # не знал как записать |x| в уравнение, пошел простейшим математическим путем и * на -1, надеюсь в математике не ошибся математика
    result_3 = f'y= : {y}'
    print(result_3)


# Есть ли какой то способ сократить код, чтобы уменьшить количество команд "Print" и при этом выводить ответ для каждого условия с строковой  частью 'y='?
# Понимаю что если в конце написать print(y) без табудяции будет выводиться только числовой ответ

# Более лаконичный вариант записи:

# result = 0
# if x > 0:
#     result = 2*x - 10
# elif x == 0:
#     result = 0
# else:
#     result = 2*x*(-1) - 1
#
# print(f'y= : {result}')