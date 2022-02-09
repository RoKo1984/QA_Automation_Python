# Напишите программу для замены последнего значения
# кортежей в списке
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

old_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# конвертирую вложенные tuple в list
new_list = []
for item in old_list:
    new_list.append(list(item))
new_list[2][2] = 100  # заменяю значение индекса вложенного list
print(f'new_list: {new_list}')
# конвертирую измененный вложенный список обратно во вложенный кортеж
tuple_in_list = []
for item in new_list:
    tuple_in_list.append(tuple(item))
print(f'tuple_in_list: {tuple_in_list}')
# присваиваю первоначальному списку новое значение
old_list = tuple_in_list
print(f'old_list: {old_list}')
