#                                                                     this a typically CQB exam model 



def new_game():
     guesses = []
     correct_gusses = 0
     question_no = 1
     for key in questions:
          print("--------------------------------")
          print (key)
          for i in options[question_no-1]: # indexing starts at zero.
              print (i)
          guess = input ("Enter A, B, C, D : ").upper()
          question_no += 1
          guesses.append(guess) 
          correct_gusses += check_answer(questions.get(key),guess)
     display_score(correct_gusses,guesses)
          
#----------------------------------------------------------------
def check_answer(answer,guess):
     if answer == guess:
          print ("CORRECT ANSWER")
          return 1
     else:
          print ("WRONG ANSWER")
          return 0
#----------------------------------------------------------------
def display_score(correct_gusses, guess):
     print ()
     print ("results ")
     for i in questions:
          print(questions.get(i),end="")
          
     print ()
     print ("guessess ")
     for i in guess:
          print (i,end="")
     print()
     print ( "correct gussess {}".format(correct_gusses))
#----------------------------------------------------------------
def play_again():
     pass

questions = {"who created python" : "A", \
     "what year was python created" : "B", \
     "python is tributed to which comedy group ?" : "C", \
     "Is the Earth round ?" : "A" }

# here is a list of list to include all the options 
options = [["A. Guido van Rossum","B. Elon Musk", "C. Bill Gates","D. Mark Zuckerburg"],
          ["A. 1989","B. 1991","C. 2000","D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python","D. SNL"],
          ["A. True","B. False","C. sometimes","D. what's earth? "]]


new_game()