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

