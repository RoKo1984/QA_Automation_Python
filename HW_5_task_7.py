# Напишите функцию для умножения всех чисел в списке. Рекурсивно

a = [1, 5, 3]
def calcMultNumbers(a):
    if a == []:
        return 1
    else:
        mult = a[0]
        mult = mult * calcMultNumbers(a[1:])
        return mult

print(calcMultNumbers(a = [4, 6, 10]))
