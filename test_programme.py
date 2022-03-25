# string datas 
'''
print ('this is my first programme ')
first_name = "rahul"
last_name = "jayan"
print (first_name + " "+last_name)
'''
# integer 
'''
age = 25
print (age)
print ( "you are "+ str(age))
'''
# floating point numbers 
'''
height = 250.5
print (type(height))
print ("you are "+str(height)+"cm long")
'''
# booliean 
'''
your_answer = True
your_choice = False
print (type(your_answer))
'''

# multiple assignment, assigning multiple value with a single line of code 

'''
name = "varun"
age = 28 
attractive = True 

print (name)
print (age)
print (attractive)

'''
'''
name, age, attractive = "varun", 28, True # multiple assignment 
print (name)
print (age)
print (attractive)
'''
'''
arun = varun = manesh = syam = 30 # if the value of multiple varibale are same 
print (arun)
print (manesh)
print (syam)
print (varun)
'''

# methods for string 

'''
name = "varun sandesh"
print (len(name))                       # to find the length of the string 
print (name.find('a'))                  # to find a character from the string 
print (name.capitalize())               # the first letter of the name os capitalize
print (name.upper())                    # to uppercase the sstring 
print (name.lower())                    # to lowercase the string 
print (name.isdigit())                  # check whether its a digit or not "bool" output 
print (name.isalpha())                  # alphabets 
print (name.count("a"))                 # count the repetation of the given alphabet
print (name.replace("a","h"))           # replace a charactor with another 
print (name.replace("varun","hari"))    # replace a charactor/string with another.
print (name*3)                          # to multiply strings, given number of times 
'''

# typecasting, conver value from one data type to another type (basics)
# it's most often used to display integer or floating point numbers along with a string data. string concatenation 

'''
x= 1    #int
y= 2.3  #float
z= "3"  #string

print (x)
print (int(y))  #temperory typecasting (float >> integer ) temperory change 
print (z)

y = int(y)      # permanently assign y as an integer value.


print (y)
print (z*3)     #here 3 is a string, hence o/p will be "z" printed in to x times 


z = int(z)      #string >> int 

print (z*3)     #integer multiplication 

print (float(x))
print (float(y))
print (float(z))

print ("x is "+str(x))
print ("y is "+str(y))
print ("z is "+str(z))
'''

# to accept user input 
# accept some inputs from the user using input()

'''
name = input('what is your name?: ')
age = int(input("how old are you ?: ")) # here accepted value is converted to an int data type (default type is string )
age +=1
print ('hello' + " "+ name)
print ("you are "+str(age)+" "+"years old now") # concatenation is only possible of same type, ie string with string only.
'''

# number functions in python 

'''
from cmath import sqrt
import math # to include math functions 

pi =3.14

print (round (pi))
print (math.ceil(pi))   # to round up to an integer. 
print (math.floor(pi))  # to round downwards. 
print (abs(pi))         # always gives a postitive number. 
print (pow(pi,2))       # to get the power of the given number. 
print (sqrt(pi))        # to obtain the square root of the given number. 
print (math.sqrt(pi))   # finding square root using math function.

x=1
y=2
z=3
a=5

print (max(x,y,z,a))    # to find the largest number among them.
print (min(x,y,z,a))    # to find the smallest number.
'''






# slicing = create a substring by extradting elements from another string.
# using         indexing[]  or    slice()
#               [start:stop:step]       slice(start,stop,step)

# begin with a starting index
'''
from logging import lastResort


name = "vikram adithya"

first_name = name[0]            #indexing starts from 0
print (first_name)              # printing the first charactor of the name 

first_name = name[1]            # print second charactor of the name 
print (first_name)

first_name = name[3]            # print the third charactor of the name 
print (first_name)



# to indexing more charactor, have mention ( starting_index:stroping_index )

first_name = name[0:4]          # starting index is inclusive; stoping index is Exclusive (total number of charactor is 4, (ie 0-3))
print (first_name)

last_name = name [7:]           # short hand operator begins @ index7( or 8th charactor), and stops till it reaches the end 
first_name = name[:6]
print (first_name)
print (last_name)

# step, in which sequence we are counting and displaying  indexing[star:stop:steps]
length = len(name)
 
pet_name = name[:length:2]       # count every second number (evennumber in this example ) 
print (pet_name)
pet_name = name[:length:3]       # count and store every 3rd charactor
print (pet_name)




                                   #reversre string 





reversed_name = name[::-1]      # to reverse a string 
print (reversed_name)
'''

# slice()
# slice( start , stop , step)

'''
website ="https://www.google.com" # error usually websites are like https://google.com and so on 
#         0123456789ABCDRFGHIJKL   A > 10 & E >14              A 10, B 11, C 12, D 13, E 14, F 15, G 16, H 17, I 18, J 19, K 20, L 21, M 22 
#         MLKJIHGFEDCBA987654321   these are negative numbers 
length = len(website)
slices = slice(12,-4)
print (website[slices])

website_2 = "https://google.com"
website_3 = "https://wikkipedia.com"

slice_1 = slice(8,-4)               # here we have removing/accepting  fixed positional charactors 
print (website_2[slice_1])
print (website_3[slice_1])
'''




# looping syntax ( if, for, while)

# if loop  << it only execute if the condition is true 



'''age = (input("how old are you?: ")) 

age = float(age) # first conver it as a floating point number 
age = round(age) # then round it to an integer 

if  age >= 18 :
    print ("you are an adult ")
elif age < 0 :
    print ("you haven't been born yet! ")
elif age == 100 : # == comparison operator, = is an assignment operator 
    print ("you are a century old!")
else :
    print( "you are a child ") # exception to all above condition.
'''


"""

# logical operators ( and , or )  
# to check whether 2 or more conditions are true or not 


temp = float(input ("what is the temperature outside?: "))
'''
if temp <= 30 and temp >= 20 :
    print ("the weather is good today!")
    print ("go outside and enjoy!")
elif temp >30 or temp <20 :
    print ("weather is bad outside! ")
    print ("stay indoors!")
'''
# not operator 
# what is true > false and what is false > true 

'''
if not(temp <= 30 and temp >= 20 ):             #complemet result of the condition 
    print ("the weather is good today!")
    print ("go outside and enjoy!")
elif not(temp >30 or temp <20) :                #if the condition is false it will execute and vice-versa (if the condition is true it  will not execute)
    print ("weather is bad outside! ")
    print ("stay indoors!")
'''

"""

# while loop ( it execuit its block as long as the condition remains true)







'''
while 1 == 1:
    print( ' help !, am inside an infinite loop ')

''''''
name = ''
while len(name) == 0 :
    name = input('enter your name : ')

print ('hello '+name)
'''

# other method 

'''
name = None
print (name)
while not name : # if name variable is none, the condition becames true, if name is defined the condition became false
    name = input ("enter your name : ")
print (name)

'''

# end of while loop 

#                                                           for loop 
#                                    a statement thar will execuit it's block of of code a limited amound of times 



#   while loop = unlimited 
#   for loop = limited 


#                                         a simple loop to count up to ten 




'''
for i in range(10):
    print (i)
for i in range (50,100): # first number is inclusive(50) and second number (100) is exclusive  (inclusive (starting) : exclusive (stoping))
    print(i)
for i in "ajay jacob koshi":
    print (i)
'''


'''
import time # we are gonna create a programme that will count down to 0 zero and execute the programme 

for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print ("happy new year ")
'''


#                                                         nested for loops  
#                                                   one loop inside another loop 




'''
rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("enter the symbol that you wanted to use: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end='')   # to prevent the cursor from entering the second line before first inner iteration is complete. To skipp the newline charactor which is attached to it by default 
    print ()# to skipp to nest line at the end of inner for loop 
'''



#                                               loop control statements 



# break  >> to terminate the loop entairly 
# continue >> skipp to next iteration of the loop 
# pass >> does nothing act as a place holder,   an empty loop may cause some syntax error, hence pass can be used as a place holder 

'''
while True:
    name = input ("enter your name ")
    if name != '':              # this condition will not execuit as long as content of name variable is empty.
       break 
    ''''''
    if name == "":              # similar to above condition 
        True
    else:
        break
    '''

#                                                       continue
# 

'''
phone_number = "123_456_789_0"

for i in phone_number:
    if i == "_":                # condition became true when it execuits a '_' symbol.
        continue                # skipp the current iteration to next one 
    print(i,end="")             # to skipp the newline charactor attached to the print build-in function.
'''

#                                                        pass case 

'''
for i in range (0,21):
    if i == 13:
        pass
    else:
        print (i)
'''




#                                                           list in python  
#                                   >> to store multiple value with in a single variable  woth []

'''
food = [ "rice","mango","mutton","banana","orange"]
print (food)

#                                 to print a single item from the variable we can use indexing which begins at zero 

print (food[3])                 # to print fourth item on the list 
print (food[0])                 # to print the first item on the list 

for i in food :                 # these are not numbers hence range variable is not used with it for the iteration, in here each element of the varaiable is copied in to i, one at a time 
    print (i)

import time                     # to provide a suitable time delay 
#                                                       functions of the lists 


time.sleep(2)
food.append("ice_cream ")       # to add an aditional value to the list, usually at the end of the list.
print (food)


time.sleep(3)
food.remove("rice")             # to remove a selected element 
print (food)


time.sleep (3)
food.pop()                      # to remove last item 
print (food)


time.sleep(3)
food.pop()                      # again removed the last item on the list 
print (food)

time.sleep(3)
food.reverse()                  # to reverse the index, last index at the begning and first content at the last 
print (food)

time.sleep(3)
food.insert(0,"grapes")         # to insert a content to a specific index with out removing any, results in shift of previous index values 
print (food)

time.sleep(3)       
food.sort()                     # to sort it 
print (food)

time.sleep(3)
food.clear()                    # to clear the list 
print (food)
'''




#                                            2D lists  1:27/12:00 (a list of list ) []



'''
drinks = ["tea","soda","coffey"]                # second element 
dinner = [",pizza","hamburger","hotdog"]
dessert = ["cake","dinner","desert"]



food = [drinks,dinner,dessert]                  # first element 

print (food)

print (food[0][0]) # to print a specific index; food[first element][second element]
print (food [0][2]) # prints coffey 

#                                                    this is a typical 2D array
'''





#                                                           tuples  ()
#                             collection which is ordered and unchangable used to group together related data 


'''
student = ("Ajay",21,"male")

print (student.count("Ajay"))       # repetations of the givent string/number 
print (student.index("male"))       # index number of this quantity 

for value in student :
    print (value)


if "male" in student:               # to check whether a value is available in the given index 
    print ("it's here")
else :
    print ("not found")
    
'''




#                                                           set {}
#                               collection which is unordered, unindexed. No duplicate value  




'''
import time                         # just included to check sets operations with suitable delay 
print ()                            # to seperate two sets 
print ()


utensils    =  {"fork","spoon","knife","fork"} # they are un orded and not allow duplicate values 
dishes      =  {"bowl","plate","cup"}

utensils.add ("napkins")            # to add an element to the set 
utensils.remove("fork")             # to remove an item from the list 
#utensils.clear()                    # to clear the set




for i in range (1,10,1):         # to check the unordered form 
    for choice in utensils :
        print (choice)
        time.sleep(2)
    print ()
    print ()


print ("items in utensils")
for choice in utensils:
    print (choice)                  # it won't print two fork 
   # time.sleep(2)

#   to add one set to another set 
utensils.update(dishes)             # adding or integrating two sets 

print ()                            # to seperate two sets 
print ()


time.sleep(5)
print ("updated utensils ")
for choice in utensils:
    print (choice)



print ()                               # to seperate two sets 
print ()


# to create a union of two sets 

dinner_table = utensils.union(dishes)   # this newly created dinner_table is a union of other two sets.
print ('items in dinner_table')
for item in dinner_table :
    print (item)


print ()                                # to seperate two sets 
print ()

# it can also used to list what a list doesn't have compared to second list 

items = {"pen","pencil","scales","ruler"}
items2 ={"marker","pen","compass","divider","ruler"}

print (items.difference(items2))        # what items have in comparison with items2 
print ()                                # to seperate two sets 

print (items2.difference(items))        # what items2 have in comparisons to items 

print ()                                # to seperate two sets 
print ()                                

print ("common in two list ")
print (items.intersection(items2))      # list what are the things that are common in two list 
print ()                                # to seperate two sets 
'''





#                                                   DICTONARY () []
#                            a changable, unorderd collection of unique KEY:VALUE pairs 
#                         fast because they used hashing allows us to acces a value quickly 




# let's create a dictonary of capitals and countries 

'''
capitals = {"INDIA":"NEW DELHI",
 "USA":"WASHINGTON DC",
 "CHINA":"BELGING",
 "RUSSIA":"MOSCOW"}
for key,value in capitals.items():
    print (key,value)

print ()
print ()                                # to seperate two sets 


print ("capital of INDIA: ",capitals['INDIA'])                       #to directly get value pair 
print  (capitals.get("germany"))                # by using ths method  we can avoid syntax error in case item is no fount in the set
capitals.pop('CHINA')                           # to remove china from the list 
capitals.update({"USA":"LOS ANGELS"})           # updating/ altering the dictonary
capitals.update({'GERMANY':'MOSCOW'})           # added a new value to the list 
capitals.key()                                  # to list all keys 
capitals.value()                                # to list all values

print ()                                # to seperate two sets 
print ()                                # to seperate two sets 

for key,value in capitals.items():
    print (key,value)


print ()                                # to seperate two sets 
print ()                                # to seperate two sets 


capitals.clear()                        # clear out the dictonary 
for key,value in capitals.items():
    print (key,value)
'''




#                                                           index operator  []
#                                                           give access to  a sequence of elements (str, list, tuples)


'''
print ()                                # to provide space  

name = "ravi varma"
if (name[0].islower()):                 # to check an element(first letter in here) of the string is lowercase 
    name = name.capitalize()

print ()                                # to provide space  

print (name)
print ()                                #to provide space 

first_name = name[:4].upper()           # make it as uppercase letters 
last_name = name[5:].lower()            # make it as lowercase letters 

last_charactor = name[-1]               # to access last element using negative indexing 
print (first_name, last_name)
'''



# ---------------------------------------------------------------funcions----------------------------------------------------
#                                                    a block of a code, execuits when it is called.
'''


def name_of_function():
    body of the function



#                                                       function definition
from re import L
from sqlite3 import DatabaseError
from tokenize import group



def hello():
    print( "hello ! BRO" )

#                                 to                    function calling 
hello ()


# to                                                    passing arguments 


def wish(data1):                                       # acceps input from calling function
    print("hello",data1)


def space():
    print()                                            #to provide space b/w two o/p datas 
    print()




wish("manu")                                           # passing a string value 
name = input("what was your name?: ")
space ()
wish(name)








def data_base(f_name,last_name=None,age = 28,group= "EC"):                         # passing multiple arguments, and predefning some arguments 
    print(f_name,last_name,age,group)
    print()









first_name = input("enter your first name: ")                  
last_name  = input("enter your last name: ")
age        = input("enter your age: ")
group      = input("enter your group: ")

data_base(first_name, last_name, age, group)                    # accepts multiple arguments 
data_base(first_name, last_name)                                # only passing two arguments 
'''








#                                                              return statements in functions 
#                                           functions send back values/objects back to the caller 
#                                           These values/obijects are known as the functions return value 




# a function to multiply two numbers are return the result to the caller 



'''
def multiply(a,b):
    print()                                                    # to provide space in b/w
    return(a*b)



a = int(input("enter the first_number : "))
b = int(input("enter the second_number : "))

product = multiply(a,b)                                       # storing the result on a varaiable
print ("the product of given numbers are : "+ str(multiply(a,b)))                                         # directly printing the result 
print ("the product of "+str(a)+" * "+str(b)+" = "+str(product))
'''









#                                  ----------------------------------------------key word arguments ----------------------------------------------
#                                                       arguments preceded by an identifier when we pass them to a function, 
#                                                      The order of the arguments doesn't matter, unlike positional arguments. 
#                                                        Python knows the names of the argumnts that our function receives









#                                        typical example for the positional arguments are

'''

def hello(f_name,m_name,l_name):
    print("hello "+f_name+" "+m_name+" "+l_name)

hello("Raja","ravi","varma")
hello("varma","Raja","ravi")


#                                                           key word arguments

hello(l_name = "varma",f_name = "Raja", m_name = "ravi")    # arguments are disoriented 

hello(m_name = "ravi", l_name = "varma", f_name = "Raja")
'''











# ----------------------------------------------------------------nested function call---------------------------
#                                                     function calls inside other function calls
#                                                     inner most function calls are resolved first 
#                                           returned value is used as arguments for the next outer function 




'''

# heare is a typicl example programme > we can use nested function to resolve this programme 

num = input("enter a whole positive number: ")
num = float(num) 
num = abs(num) 
num = round(num) 
print (num) 

# neste function example

print (round(abs(float(input("enter a whole positive number: ")))))     # begins @ the innermost layer 


'''



#----------------------------------------------------------------scope of a variable--------------------------
#                                                    a region that a variable is recognised
#                                       a varaiable is only available from inside the region it is created.
#                                       a global and locally scoped version of a variable can be created 


'''
def display_name():
    name = "test"                               # scope of the the variable is local, it is recognised only inside a function, local variable 
    print (name)

# uncomment the following 
# print (name)                                    # error the variable is not declared locally





variable = "name "  # this is a global variable which can be accessed through out the workspace, having global scope, it can also be accessed insida a function




def display_test():
    #print(variable)                             # globally declared version
    variable = "new variable"                   # locally declared version
    print (variable)                            # printing locally declared version


print (variable) # printing                     # printing the variable outside the function, to check whether it has been changed.

display_name()
display_test()



# this is how python consider variables to be variables


# L > local variable
# E > enclosing variable
# G > global variable
# B > built-in variable


'''










# ----------------------------------------------------------------                  *args                                  >> tuple     *
#                                                               parameter that will pack all arguments into a tuple 
#                                                          useful so that a function can accept a varying amount of arguments 





'''
#                                                       simple programm to add a definite number or fewer number of arguments 

def add(n1,n2):
    return(n1+n2)

print (add(1,2))

'''





#                                                                   if have more a number of arguments/parameters, then 



'''
def add(*args):                                        #  we are packing the argument in a tuple, they are orderd and unchangeable 
    sum = 0
    for i in args:
        sum += i
    return(sum)


print (add(1,2,3,4,5,6,7,8,9,10,11,12))


'''
'''

def add(*items):                                        # to make changed to tuples data  >  conver it into  list 
    items = list(items)                                 # tuples are reassigned as a list 
    items[0]= -70                                       # changing value baised on their index positions 
    sum = 0
    for i in items:
        sum += i
    return(sum)

print (add(1,2,3,4,5,6,7,8,9,10,11,12))

'''











# --------------------------------------------------------------------------   **kwargs    ------------------------------------------------------- >> dictonary   **
#                                                       parameter that will pack all arguments in to a dictonary 
#                                               usefull so that a function can accept a varying amount of keyword arguments 







#suppose we create a function that accepts two key word arguments, first name and last name. if some have an additional middle name, then a programme may occure 





'''
def sample_code(first,last):
    print( first, last)


sample_code(first = "sree", middle = "raja", last ="varma") 

'''
#                                               an error occured " TypeError: sample_code() got an unexpected keyword argument 'middle' "




#                                                       in order to overcome such sittuations we use **kwargs** instead
'''
def sample_codes(**kwargs):
    print ("hello "+kwargs["first"]+" "+kwargs["last"])             # simple approach                                      o/p hello sree varma
    print ()                                                        # to create white space 

    print ("hello",end=" ")                                         # replace the new line charactor with a space 
    for key,value in kwargs.items():
        print (value,end=" ")                                       # we only need to display values,                       o/p hello sree raja varam
    print ()                                                        # to create white space 






sample_codes(title= "Mr",first="sree",middle="raja",last="varma")
'''



















# ----------------------------------------------------------------        str.format()      ----------------------------------------------------------------
#                                              optional method that gives users more control when displaying output 




'''

# typical code writing 

animal = "cow"
item = "moon"

print ("The "+animal+" jumped over the "+item)

# now using str.format()
# "  {} " are called 'format fields', act as a place holder 


print ("The {} jumped over the {} ".format("cow","moon"))                       # insert as positional arguments  << direct assigning 
print ("The {} jumped over the {} ".format(animal,item))                        # using variables 

print ()                                                                        # creating white space 

print ("The {0} jumped over the {1} ".format(animal,item))
print ("The {1} jumped over the {0} ".format(animal,item))                      # positions has been altered 
print ("The {0} jumped over the {0} ".format(animal,item))                      # positions has been altered 
print ("The {1} jumped over the {1} ".format(animal,item))                      # positions has been altered 


print ()                                                                        # creating white space 

print ("The {item1} jumped over the {item2}".format(item1="cow", item2="moon")) # keyword arguments 
print ("The {item2} jumped over the {item1}".format(item1="cow", item2="moon")) # keyword arguments 
print ("The {item1} jumped over the {item1}".format(item1="cow", item2="moon")) # keyword arguments 
print ("The {item2} jumped over the {item2}".format(item1="cow", item2="moon")) # keyword arguments 







#                                                                   another way to print this                                                                   





print ()                                                                        # creating white space                                              

text = "The {} jumped over the {}"

print (text.format(animal,item))



# other use cases here
# adding padding 
name = "vijay"

print ("hello my name is {}".format(name))
print ("hello my name is {:10}. nice to meet you. ".format(name))               # to add some space after name, before the nice................................
print ("hello my name is {:<10}. nice to meet you. ".format(name))              # aligned to left (default )
print ("hello my name is {:>10}. nice to meet you. ".format(name))              # aligned to right (default)
print ("hello my name is {:^10}. nice to meet you. ".format(name))              # aligned to center (default)







#                                           to display a fixed number of digits after '.'
number = 3.14159




print ("The number pi is {:.2f}".format(number))                                # .'2' two positions, f >> floating point
print ("The number pi is {:.3f}".format(number))                                # 3 positions 

number = 1000
print ("The number pi is {:,}".format(number))                                  # mark a comma after 3 positions
print ("The number pi is {:b}".format(number))                                  # provide the binary o/p of the number
print ("The number pi is {:o}".format(number))                                  # provide the octal out put 
print ("The number pi is {:x}".format(number))                                  # hexadecimal o/p. x > lowercase, X > uppercase.
print ("The number pi is {:e}".format(number))                                  # display with scientific notation e or EC

'''


















#------------------------------------------------------------------------------import random ----------------------------------------------------------------
#                                                                to generat some pseudo random numbers from






'''
import random

x = random.randint(1,6)                                                         # create a random integer in b/w 1 & 6
print (x)
print ()                                                                        # creating white space                                              

y = random.random()                                                             # create a random floating point number 

print (y)
print ()                                                                        # creating white space                                              


# randomly choosing an item from the list 
my_list = ["rock","paper","scissors"]
print (random.choice(my_list))                                                  # print a random item from the list 
print ()                                                                        # creating white space                                              



# we have a collection of cards 
card = ["A",2,3,4,5,6,7,8,9,"J","K","Q"]
print ("the cards are ",card)
random.shuffle(card)                                                            # randomly shuffles the card, we may not be able to predit it.
print ("the shuffled cards are ",card )
print ("the shuffled card is {} ".format(card))
#print ("the shuffled card are {} ".format(random.shuffle(card)))               # some kind of logical error occured 

'''

















#------------------------------------------------------------------------------exception----------------------------------------------------------------
#                                                 events detected during execution that interupt the flow of the programm








'''
try:                                                      # we don't know what the user is going to input
    numerator =int(input("Enter a number to divide : "))
    denominator =int(input("Enter a number to be divided by : "))
    result = numerator / denominator
    #print (result) 




#                                                           till this block every thing is as usual as always 
#                                                       it is not a good practice to have a single exception block 


except ZeroDivisionError as e:
    print (" you can't divide by zero! idiot!")
    print (e)

except ValueError as e:
    print ("Enter only numbers pls ")
    print (e)
except Exception as e:                          # this block will catch all the exception occured during the programming rather than interrupting it 
    print ("something went wrong")
    print(e)
else:
    print (result)
finally:
    # even if some errors occure we may have to perfom some exceptions, such as closing a file.
    print(" this statge will always execuit")




'''

