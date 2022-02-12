# За день машина проезжает n километров. Сколько дней нужно, чтобы
# проехать маршрут длиной m километров? Программа получает на вход
# числа n и m.


n = float(input("Enter the distance that the car travels in one day in kilometers:  " ))
m = float(input("Enter the total distance to be driven in kilometers:  " ))

t = int((m//n)) # перевожу в int чтобы не отображать дробную часть в виде 0

time = "The trip will last:{distance} day(s)".format(distance=t)

print(time)
