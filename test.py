# this is a test revew that i just made just now.

def new_game():
     print ("----------------------------------------------------------------")
     print ()
     print ()
     answers = []
     count = 0
     score = 0
     for items in questions:
          print ("\n {} \n".format(items))
          for i in options[count]:
               print (i,end=' ')
          answer = (input("\nEnter your choice \n\n A B C D : ").upper())
          answers.append(answer)
          print ()
          print ()
          score += check_answer(questions.get(items),answer)
          count += 1
     display_score (answers,questions,score)
def check_answer(answer,gusses):
     if answer == gusses:
          print ("CORRECT")
          return 1
     else:
          print ("WRONG")
          return 0
def display_score(keys,gusses,score):

     print ("your gusses")
     for j in keys:
          print (j,end="")
     print ()
     print ("Actual answers ")
     for key in gusses:
          print (gusses.get(key),end="")
     print ()
     print (score)
     #score_1 = (score/(len(questions))*100)
     print ('score is {}'.format(score/(len(questions))*100))

def play_again():
     responce = input ("Do you want to play \n\n\t\tY/N\t:\t").upper()
     if responce == 'Y':
          return True
     elif responce == 'N':
          return False
     else:
          print ("invalid input ")

questions = {"who created python" : "A", \
     "what year was python created" : "B", \
     "python is tributed to which comedy group ?" : "C", \
     "Is the Earth round ?" : "A" }

# here is a list of list to include all the options 
options = [["A. Guido van Rossum","B. Elon Musk", "C. Bill Gates","D. Mark Zuckerburg"],
          ["A. 1989","B. 1991","C. 2000","D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python","D. SNL"],
          ["A. True","B. False","C. sometimes","D. what's earth? "]]

while play_again():
     new_game()