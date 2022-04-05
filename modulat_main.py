#                                           part 1

'''
import modular_sub                      # this a sub module located in same directory to store function definition files

modular_sub.hello()
modular_sub.bye()
'''







'''
import modular_sub as msg              # import the function/ module as msg 

msg.hello()
msg.bye()
'''










'''
from modular_sub import hello,bye     # directly importing the function from the module 

hello ()
bye ()
'''








'''from modular_sub import *            # to import all the function from a modul 

# it is usually not recommented for larger programme, nameing conflits may occure


hello ()
bye ()
'''


# go check for python modules from the internet 




#----------------------------------------------------------------simple game developement ------------------------------------------------------------------------

import random # random

choices = ['rock','paper','scisseors']
computer = random.choice(choices) #select a random choice from the list 
# print (computer)                # to print computer choice 
player = None

while player not in choices:
     player =input ("rock\tpaper\tscisseors\t:").lower() # player input is converted in to lower case 

print ("computer\t {}".format(computer)) # 
print ("user\t\t {}".format(player))