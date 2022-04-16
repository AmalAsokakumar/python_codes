# -----------------------------------------------------------------        lambda function     -------------------------------------------------------------------------
#                                                     function writtern in 1 line using lambda keyword
#                                               accepts any number of arguments, but only has one expression.
#                                                                                                             (think of it as a shortcut )
#                                                                                                             (useful if needed for a short peroid of time, throw-away)
#                                                                                                              mostly used we we need to uses a function once, not repetely 
# lamada parameter:expression




"""

sort ()

map ( funtion, iterable )

filter (function, iterable)


functools.reduce( function, iterable ) # import functools
"""












'''
def double(x):
     return x * 2

print (double(5))


# as a lambda function 
double_1 = lambda x:x*2
print (double_1(10))

# have 2 number to multiply
multiply = lambda x,y:x*y 
print ("the product is : "+str(multiply (8,5))) # type cast to convert the return data type as a string for string concatenation.

#lets add 3 numbers together


add = lambda x,y,z:x+y+z
print (x:=10,y:=15,z:=12,"\nThe sum of three numbers are {} + {} + {} = {}".format(x,y,z,add(x,y,z)))

print (x:=3,y:=2,z:=4,"\nThe product of {} + {} + {} = {}".format(x,y,z,lambda x,y,z:x*y*z))
sum = lambda x,y,z:x*y*z
print (x:=3,y:=2,z:=4,"\nThe product of {} + {} + {} = {}".format(x,y,z,sum(x,y,z)))

full_name = lambda first_name,last_name: first_name + " " + last_name
print (full_name("varun","sharma"))

# a simple lambda function to check age of a person in

age_check = lambda age:True if age >= 18 else False
print (age_check (int(input("Enter your age : "))))  # int < type converter, default input is considered as a string value 


'''































#----------------------------------------------------------------                sort()                   ----------------------------------------------------------------
#                                                                   sort () method  >> used with list 
#                                                                sort () function >> used with iterables



'''

# here is a list called students []
from turtle import st


students = ["Squidward","sandy","patrick","Spongeboob","Mr. Krabs"]

students.sort() # we can provide two arguments in this function.   >>  "" reverse = true ""  and "" key """
for i in students:
     print (i)
print ("\n")


# sorted in reverse order.
students.sort(reverse=True)  # it only going to work with list not with 'tuple ()',  'list []'
for i in students:
     print(i)                # here it will print in reverse order.
print ("\n")




# here we are using a tuple 
students = ("Squidward","sandy","patrick","Spongeboob","Mr. Krabs")
# in here sorted student is a list[]
sorted_students = sorted(students) # << accepts tuples as an arguments...  or 'sorted' convert it as an argument
for i in sorted_students:
     print (i)
print ("\n")




# for reverse order 
sorted_Students = sorted(students,reverse=True)
for i in sorted_Students:
     print (i)
print ("\n")








#                                                                               part 2
# now here we have a list of tuples of students
# here we are going to use 'key' keyword argument 


students = [("SquidWard","F",60),
            ("Sandy","A",33),
            ("Patrick","D",37),
            ("Spongebob","C",39),
            ("Mr. Khan","S",26)]

students.sort()                    # here the list is sorted based on first coloumn

for i in students:
     print (i)
print ("\n")



# in order to sort it based on other coloum we use " key " kewword argument
"""
we set key equlas to a function that is going to return the index of the that specific coloumn that we have 
"""

grade = lambda grades:grades[1]                                 # indexing start from zero, coloumn 2's index "1", and for coloumn '3' is "2"
students.sort(key=grade)                                        # grade is going to be a function obiject via loambda functions
for i in students:
     print (i)
print ("\n")



students.sort(key=grade,reverse=True)                           # to print in reverse orde 
for i in students:
     print (i)
print ("\n")



#                                       similarly we can also change it according to the age of the students
print ("\n")


age = lambda age:age[2]
students.sort(key=age)

for i in students:
     print (i)

students.sort(key=age,reverse=True)                              # in reverse order 
for i in students:
     print (i)

'''







#                                                                suppose we have a tuples of tuples 


'''

from audioop import reverse


students = (("SquidWard","F",60),
            ("Sandy","A",33),
            ("Patrick","D",37),
            ("Spongebob","C",39),
            ("Mr. Khan","S",26))

age = lambda ages:ages[2]
sorted_students = sorted(students,key=age)  

for i in sorted_students:
     print (i)
print ("\n")


sorted_students = sorted(students,key= age,reverse=True) #                      sorted in reverse order 
for i in sorted_students:
     print (i)

# 4:53/12:00


'''
















































# ---------------------------------------------------------------------         map()        ----------------------------------------------------------------
#                                                 applies a function to each item in an iterable( list, tuple, etc )
#                                                                   map (function, iterable)

# suppose we have an online store for

'''
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]


# simply print the list of items

for i in store:
     print (i)
# to convert mov=ney form one us doller to euros 

to_euro = lambda data: (data[0],data[1]*0.82) # lambda function to conver currency 
store_euros = list(map(to_euro,store))  # map fiunction applies a function to each item in an iterable.

print("\n")

for i in store_euros:
     print (i)
'''

































# ----------------------------------------------------------------------    filter ()   -------------------------------------------------------------------------
#  create a collection of elements from an iterable for which a function returns True

#filter(function, iterable)


'''

friends = [ ("syam",16),
            ("varun", 18),
            ("varun",20), 
            ("dinesh",16), 
            ("vimal",17), 
            ("vasanthan", 22)]
  


# creare a seperate list for those that are 18 and older 

age = lambda data:data[1] >= 18

drinking_buddies =list(filter(age,friends)) # filtered value is converted into a list.

for i in drinking_buddies:
     print (i)


'''

# end



































#----------------------------------------------------------------        reduce ()     ----------------------------------------------------------------
#                                       apply a function to an iterable and reduce it to a single cumulative value.
#                                     perfoms function on first two elements and repeates  process until 1 value remains 

# reduce ( functinon, iterable )



# list of iterable 
'''

import functools

letters = ["H","E","L","l","0"] # we need to reduct this in to single cumulative value to



word = functools.reduce(lambda x,y :x+y,letters)

print (word)


""" reduce function selects the first 2 elemnts in "letters" and prfoms the lambda function "x+y",
then we perfoms this operation again as x = "x+y" and choose other letter as y  (x=(x+y) >> HE,  &  y >> L)
this openation continues until there is a single element left .
"""


factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y, factorial)

print (result)
'''


































































