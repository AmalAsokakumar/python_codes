'''
class Animal:                      # this act as parent class << which has everything which is common in other classes 

     alive = True 


     def eat(self):
          print ("This animal is eating")

     def sleep (self):
          print ("This animal is sleeping")

#                                                           lets make a class for other animals 

"""
in here Animal class act as a parent class 
where as Rabbit, fish and hwak act as a child class which
as mentioned, child class will inheret all the features of the parent class
"""
class Rabbit(Animal):              # this class act as a child class which is going to inheret everything from the parent class 
     def run (self):
          print ("This rabbit is running ")
class Fish  (Animal): # 
     def swimming (self):
          print ("This fish is swimming ")
class Hwak (Animal): 
     def fly (self):
          print ("This bird is flying")

rabbit    = Rabbit()               # here we are creating an obiject 
fish      = Fish()                 # here we are creating an obiject 
hwak      = Hwak()                 # here we are creating an obiject 


print (rabbit.alive)
fish.eat()
hwak.sleep()
rabbit.run()
fish.swimming()
hwak.fly()
'''







































# ----------------------------------------------------------------  multi level inheritance  ----------------------------------------------------------------
#                                              when a derived (child) class inherits another derived (child) class.


'''
class Organism:

     alive = True

class Animal(Organism):                                     # here Animal class inherets from the parent class;  child << parent 

     def eat (self):
          print ("This animal is eating ")

class Dog (Animal):                                         # here Dog class << inherits << from  Animal class;  child << child 
     def bark (self):
          print ("This dog is barking ")




dog = Dog()  # here we are creating an obiject 

print (dog.alive)
dog.eat()
dog.bark()
'''





































# ----------------------------------------------------------------      multiple inheritance ----------------------------------------------------------------
#                                                     when a child class is derived from more than on parent class 



'''
class Prey:
     def flee(self):
          print ( "This animal is fleeing ")


class Predator:
     def hunt(self):
          print ("This animal is hunting ")


class Rabbit (Prey):                                         # here  the Rabbit class is a child class which inherits from Prey
     pass 

class Hwak (Predator):
     pass

class Fish (Prey,Predator):                                  # here is a example for multilevel inheritance 
     pass 

rabbit    = Rabbit()                    # here we are creating an obiject
fish      = Fish()                      # here we are creating an obiject
hwak      = Hwak()                      # here we are creating an obiject

rabbit.flee()
fish.flee()
fish.hunt()
hwak.hunt()
'''



#                                                                    method overwriting 
# this method will implement the one which is associated with it, insted of attaching/implementing the one which is inhereted from the parent class.


'''
class Animal:

     def eat(self):
          print ("this animal is eating ")

class Rabbit(Animal) :
     def eat(self):
          print ("This rabbit is eating a carrot ")


rabbit = Rabbit() # here we are creating an obiject
rabbit.eat()
'''



























# ----------------------------------------------------------------    method chaining   ------------------------------------------------------------------------------------
#                                                         calling multiple methods sequentially 
#                                            each call perfoms an actinon on the same obiject and return self 




'''
class Car:


     def turn_on(self):
          print ("You start the engine")
          return self                      # method chaning returns value 

     def drive(self):
          print ("You drive the car")
          return self          
     def brak(self):
          print ("You step on the break")
          return self                   
     def stop(self):
          print ("You stop the car")



car = Car()

car.turn_on()
car.drive()

# calling using method chaning 

car.drive()\
     .brak()\
     .stop()                     # this is a typical example for method chaning ... ' \ ' <<< line continuation charactor 

car.turn_on().drive().brak().stop() # use sequentially ( in the order which is created)

'''

































# ----------------------------------------------------------------------     super()     ----------------------------------------------------------------------
#                                                 function used to give access to the method of a parent class.
#                                                     return a temperory obiject of a parent class when used 








'''
class rectangle:                                       # parent class 
     pass

class Square(rectangle):                              # children class

     def __init__(self, length, width):
          self.length = length
          self.width = width



class Cube(rectangle):                                  # children class 

     def __init__(self, length, width, height):
          self.length = length
          self.width = width
          self.height = height


square = Square( 3, 3)
cube = Cube(3,3,3)

'''

'''
in here we used same line of codes for both cube and square to get length and width 
usuall we don't like to repeate the codes we just like to reuse them insted 
hence we can place them in rectangular class and reuse them later 
'''



'''
class Rectangle :
     
     def __init__(self, length, width ):
          self.length = length
          self.width = width


class Square (Rectangle):

     def __init__(self, length, width):
        super().__init__(length, width)

     def Area(self):
          return self.length * self.width

class Cube (Rectangle):
     def __init__(self, length, width, height):
          super().__init__( width, length)
          self.height = height

     def Volume (self):
          return self.length * self.width * self.height

cube = Cube(3,3,3)                      # here we are creating an obiject
square = Square(2,4)


print (cube.Volume())
print (square.Area())
'''

































# ------------------------------------------------------------------------------  abstract ------------------------------------------------------------------------------

# prevents a user from creating an obiject of that class
# compels a user to override abstract methods in a child class


# abstract class = a class which contains one ore more abstract methods.
# abstract method = a method that has a decleration but but does not have an implementation.


'''
from abc import ABC, abstractmethod # abc >> abstract base class 

class Vehicle(ABC):
     @abstractmethod
     def go(self):
          pass
     @abstractmethod
     def stop(self):
          pass
class Car(Vehicle):
     def go(self):
          print ("You drive the car ")
     def stop(self):
          print ("Stop the car")

class Motorcycle(Vehicle):
     def go(self):
          print ("You ride the motorcycclear ")
     def stop(self):
          print("Stop the motorcycle")
car = Car()
#vehicle = Vehicle() # by iclulding @abstractmethod we prevented vehicle from creating an obiject 
motorcycle = Motorcycle()

car.go()
car.stop()
motorcycle.go()
motorcycle.stop()
#vehicle.go()
#car.stop().go() # not working 
'''






























#                                                               passing obiject as argument in python 


'''
class Car:

     color = None 

class Motorcycle:
     color =None 


def change_color(Vehicle,color):
     Vehicle.color = color

car_1 = Car()            # these are the newly created obijects 
car_2 = Car()            # these are the newly created obijects 
car_3 = Car()            # these are the newly created obijects 
bike_1 = Motorcycle()    # these are the newly created obijects 


change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)


'''







































# -------------------------------------------------------------------       Duck typing      ----------------------------------------------------------------
# concept where the class of an obiject is less important than the methods/attributes
# class type is not checked if minimum method/attribute are present 
# " if we walk like a duck, and it quacks like a duck, then it must be a duck"



'''

class Duck:
     def walk(self):
          print ("This duck is walking ")

     def talk(self):
          print ("This duck is qwuacking")

class Chicken:
     def walk(self):
          print ("This chicken is walking")

     def talk(self):
          print ("This chicken is clucking")

class Person:

     def catch (self,duck): # here 'duck' act as a simple carrier to carry the date which is transfer to this fn by calling function.
          duck.walk()       # actually the data inside this varibale can be "chicken,duck or anyhing else"
          duck.talk()

          print ("You caught the critter")



duck = Duck()
chicken = Chicken()
person = Person()


person.catch(duck) # o/p of executing this function is given bellow 

"""This duck is walking 
This duck is qwuacking
You caught the critter"""


person.catch(chicken)

"""This chicken is walking
This chicken is clucking
You caught the critter"""



'''


































#    ----------------------------------------------------------------   walurus operator  ' := ' ----------------------------------------------------------------
#    new to python 3.8
#   " assignment expression " aka walurus operator 
#    assigns values to variables as part of a larger expression 


'''
happy = True
print (happy)

# lets compain above expression using walurus operator 

print (happy := True)  # here we are assigning value to a variable, as part of a larger expression 
print (happy)







"""
foods = list()
while True:
     food = input("What food do you like?:   ")
     if food == "quit":
          break
     foods.append(food)


"""

# lets write this code using walurus operator


foods = list()
while food := input("What food do you like?: ") != "quit":
     foods.append(food)

'''




























#                                                            adding a function to a variable 
#04:31/12:00





'''
def hello():
     print ("Hello")


hello()
print(hello) # will print the memory address of the hello function <. hello(hello)

hi = hello # this will also shows the address of the hello function <. hi(hello)
print(hi)


hi()  # if we execuit this function this will perfom hello function and prints "Hello"

# we can execui this hello function using hi() or hello()
# another example would be 


say = print # here we are assigning the memory address of 'print' fn. to the 'say' variable and

say ("WOW here i can print without using print fn directly ") # these are typical examples for adding function to a variable

'''








































# ----------------------------------------------------------------     High order function      ----------------------------------------------------------------
#                                                a function that either 
#                                                                    1. accept a function as argument 
#                                                                    2. returns a function 
#                                                      (in python, functions are also treated as obijects )



# eg 1  accept a function as argument
'''

def loud(text):
     return text.upper()

def quiet (text):
     return text.lower()

def hello(function):
     text = function("hello")
     print (text)

hello(loud)
print ("\n")
hello(quiet)



# eg 2  returns a function


def divisor(x):               #1
     def divident(y):         #2
          return y/x          #3
     return divident          #4             returning the address of a fn as an argument


divide = divisor(2)           #5             storing memory address of function 
print (divide(10))            #6 


"""
in here we execute the programmm 
#5 will execute and assign 'x' as '2' 
#2 and #3 won't be executing since it isn't called 
#4 returns address location of divident function 


when executing #6 'divide' fn.  which has the address of divident function, which is being called and passed an argument '10' to it 
#2 will execuit, in here value of 'x' is set during previous execution (#5), now we provided the y argument. The result of execution will be returned by "return fn."
and will be printed.


 """



'''








































# -----------------------------------------------------------------        lambda function     -------------------------------------------------------------------------
#                                                     function writtern in 1 line using lambda keyword
#                                               accepts any number of arguments, but only has one expression.
#                                                                                                             (think of it as a shortcut )
#                                                                                                             (useful if needed for a short peroid of time, throw-away)
#                                                                                                              mostly used we we need to uses a function once, not repetely 
# lamada parameter:expression


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




  



























