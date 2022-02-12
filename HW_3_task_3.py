# Напишите программу Python для построения следующего шаблона,
# используя вложенный цикл for.


Height =  int(input("Введите высоту треугольника: "))
for line_number in range(1, Height + 1):
        print("*" * line_number)
for line_number in range(1, Height + 1):
        print("*" * (Height - line_number))

