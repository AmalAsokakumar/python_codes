# python obiject oriented programming  POOP
# with class we can discribe an obiject and what it does 
# using __init__ mode 
# here we can create some obijects 

from car import Car 

car_1 = Car("chevy","corvertte","2021","blue")


print (car_1.make)
print (car_1.model)
print (car_1.year)
print (car_1.color)

car_1.drive()
car_1.stop()

car_2 = Car("Ford","Mustang","2022","Red")

print (car_2.model)
print (car_2.year)
print (car_2.color)
print (car_2.make)
car_2.drive()
car_2.stop() 


# 
print (car_1.wheels)
print (car_2.wheels)


# to access a class variable 

#car_1.wheels = 2  # assume it as mortor cycle 

print (car_1.wheels)
print (car_2.wheels)


# to print class variables 


print ("Printing the class variable ")
print (Car.wheels) #print (class.variable)


# to change class variable entair instances 

print ( "reassigning the class variable ")
Car.wheels = 6


print (car_1.wheels)
print (car_2.wheels)