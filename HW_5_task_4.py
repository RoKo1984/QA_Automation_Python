#  Создайте функцию showEmployee () таким образом, чтобы она
# принимала имя сотрудника и его зарплату и отображала и то, и
# другое. Если в вызове функции отсутствует зарплата, присвойте
# зарплате значение по умолчанию 9000.

# Вариант №1

name = input("введите Имя сотрудника: ")
salary = input("введите зарплату сотрудника = ")

def showEmployee (name, salary):
    if not salary:
        salary = 9000
    if int(salary) <= 0:
        salary = 9000
        return print(f'\nИмя сотрудника:  {name} \nЗарплата сотруднака = {salary}')
    else:
        return print(f'\nИмя сотрудника:  {name} \nЗарплата сотруднака = {salary}')

showEmployee(name, salary)


# Вариант №2

# name = input("введите Имя сотрудника: ")
# salary = input("введите зарплату сотрудника = ")
#
# def showEmployee (name, salary=9000):
#
#         return print(f'\nИмя сотрудника:  {name} \nЗарплата сотруднака = {salary}')
#
# # showEmployee(name, salary) # В этом варианте есть ошибка. Выводится или значение заданное значение ЗП или пустая строка
#
# showEmployee(name) # Или выводится все время 9000.
