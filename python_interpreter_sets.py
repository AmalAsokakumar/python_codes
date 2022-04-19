# ------------------------------------------------------------------------------
# if __name__ ==' __main__'
#------------------------------------------------------------------------------



# t rho ?
# 1. Module can run as a stand alone progrmme.
# 2. Module can be imported and used by other modules



# Python interpreter sets "special variables ", one of which is  _ _ name _ _
# then python will execuit the code founded withe in __main__

#if __name__ == '__main__':
#    pass



# Python interpreter sets "special variables ", one of which is  _ _ name _ _
# Python will asign the _ _name _ _ variable a value of ' _ _ main_ _' if it's the initial module being run 
# We can test it by running print (__name__)


# suppose we import module two and check this again to

'''
import python_interpreter_sets_module2

print (__name__) # o/p >> __main__
print (python_interpreter_sets_module2.__name__) # when import another module, the name variable will be assigned the name of the module (imported module)

print (__name__) # o/p >> __main__
'''

'''if __name__ == "__main__":
     print ("running this module directly ")
else:
     print ("running outside of the programme ")
'''

def hello():
     print ("Hello")

if __name__ == "__main__":
     hello()