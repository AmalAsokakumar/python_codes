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




