class Car:     # here car is a obiject and it is being discribed  
     # obiject also have methods ( action )
     # the special method that will create obiject for us 
     # __init__ initialize 
     # here we dont need to pass any argument for the self variable 


     # class variable is declared inside the class and out side the constructor 


     wheels = 4 # this is a class variable 




     def __init__(self,make,model,year,color):   # this is called a constructor << this will create objects  
          self.make      = make    # instance variables 
          self.model     = model   # instance variables 
          self.year      = year    # instance variables 
          self.color     = color   # instance variables 
    

     def drive(self): # self means the argument using this function, or the obiject that we are currently working on 
          #print ("This car is driving ")
          print  ("This {} is moving ".format(self.model))

     def stop(self):
          #print ("This car is stopped ")
          print ("This {} is stopped".format(self.model))