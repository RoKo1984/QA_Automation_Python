word = input("Input a word to reverse: ")

for indx in range( len(word) - 1, -1, -1):
  print(word[indx], end=" ")


