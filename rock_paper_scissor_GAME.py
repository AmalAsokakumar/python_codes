import random # random

while True:
          choices = ['rock','paper','scisseors']
          computer = random.choice(choices) #select a random choice from the list 
          # print (computer)                # to print computer choice 
          player = None

          while player not in choices:
               player =input ("rock\tpaper\tscisseors\t: ").lower() # player input is converted in to lower case 

          print ("computer\t {}".format(computer)) # 
          print ("user\t\t {}".format(player))

          if player == computer :
               #print ("Computer \t :{},\nPlayer \t\t:{}\n\n\t\t\t{}".format(computer,player,"tie"))
               print("\t\ttie")

          elif (computer == "paper") and (player == "scisseors"):
               print ("you won!")
          elif (computer == "paper") and (player == "rock" ):
               print ("you loose!")
          elif (computer == "scisseors") and (player == "rock" ):
               print ("you won!")
          elif (computer== "scisseors") and (player == "paper"):
               print ("you loose!")
          elif (computer == "rock") and (player == "paper"):
               print ("you won!")
          elif (computer == "rock") and (player == "scisseors"):
               print ("you loose!")
          else:
               print ("unknown error ")
          play_again = input(" Play again? (yes/no):  ").lower()

          if play_again != "yes":
                break 
print ("bye")