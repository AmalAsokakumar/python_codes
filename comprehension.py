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






































#   ----------------------------------------------------------------   Directory Comprehension  ----------------------------------------------------
#                              create a dictionaries using an expression can replace for loops and certain lambda functions

# dictonary ={key: expression      for (key,value) in iterable }
#dictonary = {key: expression      for (key,value) in iterable if condition}
#dictonary = {key: (if/else)       for (key,value) in iterable }
#dictonary = {key: function(value) for (key,value) in iterable}



# temperatuer in few cities are list 

'''
cities_in_f = {"New York" : 33, "Bostan" : 75, "Los Angels": 100, "chicago": 50}


# temperature in clecious temperature

#dictonary = {key: function(value) for (key,value) in iterable}
cites_in_c = {key: round(((value-32)*(5/9))) for (key,value) in cities_in_f.items()}  # here .items() is used because dictionary 
print (cites_in_c)

#05:13/12:00
#dictonary = {key: expression      for (key,value) in iterable if condition}
weather = {"New York":"snowing","Bostan":"sunney","Los Angeles":"sunney","Chicago":"cloudy"}
sunney_weather = {key: value for(key,value) in weather.items() if value == "sunney"}         # dont forget to include .item()

print (sunney_weather)

# discription a bout each cities temperature sensor

#dictonary = {key: (if/else)       for (key,value) in iterable }
dis_cities = {key: "Warm" if value > 40 else "Cold" for (key,value) in cities_in_f.items()}
print (dis_cities)

#dictonary = {key: function(value) for (key,value) in iterable}
def check_temp (value):
     if value >= 70:
          return "Hot"
     elif 69>= value >= 40:
          return "Warm"
     else:
          return "Cold"

new_cities = { key: check_temp(value) for (key,value) in cities_in_f.items()}

print (new_cities)
'''










































#   ----------------------------------------------------------------      zip (*iterable)     ----------------------------------------------------------------
#                                             aggregate elements form two or more iterables (list, tupiles, set, etc)
#                                            creates a zip obiject with paired elements stored in tuples for each element 


# here i have 2 set of iterable list
'''



user_name = ["Dude", "Bro", "Mister"]
password = ("pAssword", "@bc123", "gues!")   # its a tuple 

log_in_dates = ["1/1/2022","1/2/2022","1/3/2022"]



# create a zip obiject 
"""
users = zip (user_name, password)

for i in users:
     print (i)

     
print (type(users)) # print data type 
users =list (users) # to convert is a list 
print (type (users))
"""






# to convert the list as a dictonary key:value pair 
"""
users = dict(zip(user_name, password))

for key,value in users.items():
     print (key+" : "+value)

"""




# create a list of more than two iterable 

users = zip(user_name, password, log_in_dates)

for i in users:
     print (i)



'''















































