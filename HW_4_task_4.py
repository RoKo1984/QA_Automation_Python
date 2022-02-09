# Напишите программу, которая проверяет, присутствует ли А в
# наборе или нет. А вводится с клавиатуры

x = input('Введите любую букву латинского алфавита: ' )
fraise = input("Введите любую фразу: " )
fraise = set(fraise)
print(x)
print(type(fraise), fraise)
if x in fraise:
    print("yes")
else:
    print("no")
