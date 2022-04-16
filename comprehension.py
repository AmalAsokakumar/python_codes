# ----------------------------------------------------------------------   list comprehension function   ----------------------------------------------------------------
#                                                                a way to create a new list with less syntax 
#                                                           can mimic certain lambda functions, easier to read 
#                                                                                                        list = [ Expression for item in iterable ] 
#                                                                                                        list = [ Expression for item in iterable if conditional]
#                                                                                                        list = [ Expression if/else for item in iterable ]
#



# simple example to create square for a group of items

'''
square = []                                                 # creating an empty list 

for i in range (1,11): 
     square.append(i*i)                                     # appending to the empty list

print (square)                                              # printing the result 

# we can write the same code using list comprehension syntax error
#                                                                                                        list = [ Expression for item in iterable ] 
                                                                                                  
#  list = [ Expression for item in iterable ] 
squares = [i*i for i in range (1,11)]                       # we have create above programme using less syntax 
print (square)




students = [100,90,80,70,60,50,40,30,20,10,0]


passed_students = list(filter(lambda x:x >50, students))    # using lambda function  
print ("passed students "+ str(passed_students))



#                                                                                                        list = [ Expression for item in iterable if conditional]
#          list = [ Expression for item in iterable if conditional]
passed_students = [ i for i in students if i >50 ]
print ("passed students "+ str(passed_students))



#                                                                                                        list = [ Expression if/else for item in iterable ]
#          list = [ Expression if/else for item in iterable ]
passed_students = [i if i >60 else "FAILED" for i in students]
print ("passed students "+ str(passed_students))
'''


















