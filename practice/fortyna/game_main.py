import fortyna.game_administrative as admin
import random as rnd
def is_win(word):
  if "*" in word:
    return False
  else:
    return True
def play(words = admin.read_words()):
  points = 0
  while True:
    if(len(words)==0):
      print("nice game!)")
      admin.update_record(points)
      print("Your record is:" + str(admin.get_record()))
      break
    answer = str(input("Хотите сыграть? y/n"))
    if(answer == "n"):
      print("See you later :)")
      break
    word = words[rnd.randint(0, len(words)-1)]
    word_matrix = ["*" for i in range(0, len(word))]
    lives = admin.read_lives()
    while True:
      for i in range(0,len(word)):
        print(word_matrix[i], end="")
      print(f" | lives: {lives}")
      symbol = str(input("Type new char"))
      if (symbol == word)and(symbol != word[0]):
        print("You win! All word")
        points+=10
        words.remove(word)
        break
      if(symbol in word):
        for i in range(0,len(word)):
          if(symbol == word[i]):
            word_matrix[i] = word[i]
            points += 1
        if(is_win(word_matrix)):
          print("You win! By char")
          words.remove(word)
          break
      else:
        lives-=1
        if(lives==0):
          print("You lose!")
          break