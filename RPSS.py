from random import *

win = 0
loss = 0
tied = 0

while(True):
  items = ["Rock", "Paper","Scissors", "Lizard", "Spock"]

  for i in range(5):
      print(i+1, items[i])

  playerchoice = -1
  while(playerchoice > 5 or playerchoice < 1):
      playerchoice = int(input("Make your choice: "))

  print("You chose:", items[playerchoice - 1])





# if player chose rock
  if (playerchoice == 1):
      cheatlist = [1,2,3]
      cpuchoice = cheatlist[randint(0,2)]
      if cpuchoice == 2 or cpuchoice == 5:
          print("you lose")
          loss +=1
      else:
          print("You Lose!")
          loss +=1

# if player chose paper
  elif (playerchoice == 2):
      cheatlist = [2,3,5]
      cpuchoice = cheatlist[randint(0,2)]
      if(cpuchoice == 1 or cpuchoice == 5):
          print("You won!")
          win += 1
      else:
          print("You Lose!")
          loss += 1

# if player chose scissors
  elif (playerchoice == 3):
      if(cpuchoice == 2 or cpuchoice == 4):
          print("You won!")
          win += 1
      else:
          print("You Lose!")
          loss += 1

# if player chose lizard
  elif (playerchoice == 4):
      if(cpuchoice == 2 or cpuchoice == 5):
          print("You won!")
          win += 1
      else:
          print("You Lose!")
          loss += 1

# if player chose spock
  elif (playerchoice == 5):
      if(cpuchoice == 1 or cpuchoice == 3):
          print("You won!")
          win += 1
      else:
          print("You Lose!")
          loss += 1

  print()
  print("win = ", win, "loss=", loss, "ties=", tied)
  print("Lez Go Again")
  print()