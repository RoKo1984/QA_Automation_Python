# Напишите программу Python, которая принимает слово от
# пользователя и переворачивает его
# Пример:
# input - Hello Worlds
# output - sdlroW olleH

word = input("Input a word to reverse: ")

for indx in range( len(word) - 1, -1, -1):
  print(word[indx], end=" ")


