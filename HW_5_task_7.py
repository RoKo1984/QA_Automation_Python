# Напишите функцию для умножения всех чисел в списке. Рекурсивно

def calcMultNumbers(list):
    if list == []:
        return 1
    else:
        mult = list[0]
        mult = mult * calcMultNumbers(list[1:])
        return mult

print(calcMultNumbers(list = [4, 5, 10]))
