import random as rnd

def is_win(word):
  print(len(word))
  counter = 0
  for i in range(0,5):
    if(word[i]=="*"):
      counter +=1
  if(counter == 0):
    return True
  else:
    return False


words = ["книга", "месяц", "ручка", "шарик", "олень", "носок"]

while True:
  if(len(words)==0
     ):
    print("nice game!)")
    break
  answer = str(input("Хотите сыграть? y/n"))
  if(answer == "n"):
    print("See you later :)")
    break
  word = str(words[rnd.randint(0, len(words)-1)])
  word_matrix = ["*","*","*","*","*"]
  lives = 5
  while True:
    for i in range(0,5):
      print(word_matrix[i], end="")
    print(f" | lives: {lives}")
    symbol = str(input("Type new char"))
    if (symbol == word):
      print("You win!")
      words.remove(word)
      break
    if(symbol in word):
      for i in range(0,5):
        if(symbol == word[i]):
          word_matrix[i] = word[i]
      if(is_win(word_matrix)):
        print("You win!")
        words.remove(word)
        break
    else:
      lives-=1
      if(lives==0):
        print("You lose!")
        break

