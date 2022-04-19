'''
import time




"""
print (time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
#  epoch = when your computer thinks time begins (reference point)


print (time.time()) # return current seconds since epoch 
print (time.ctime(time.time())) #2ill get current time 

# time.strftime( format, time_obiject) << formats a time obiject to string 
time_obiject = time.localtime()     #gets local time 
time_obiject = time.gmtime()       # utc time 
local_time = time.strftime("%B  %D %Y %H %M %S", time_obiject)
print (local_time)

"""


"""
print (time.ctime(100000)) 
print (time.time())

# to print current time using above two method 

print (time.ctime(time.time())) # time.time will return the amound of time since our epic and ctime will conver it in a redable string 
"""





# to get current time using local time method 


"""
local_time_obiject = time.localtime() #
print (local_time_obiject)
print (type(local_time_obiject))
# local time obiject is refered to as a struct time obiject, which is made up of different key word arguments 
# to convert above time obiject to a readable format we use time.strftime(format, time_obiject)  "strftime">> string format time 
# check offical webstie for getting a detailed discription of chractors that we can use to convert
print ("The local time is : "+time.strftime("%B %D %Y %H:%M:%S",local_time_obiject))#%B name of the month, %D date , %Y year, %h hour, %m minute, %s seconds. 
print ("The utc time is : "+time.strftime("%B %D %H:%M:%S",time_obiject := time.gmtime()))


"""






"""
time_string = "20 April, 2022"
time_obiject = time.strptime(time_string,"%d %B, %Y") # this function will phras a string representation of a time or date and return a time obiject, 
# so we just need to pass in a string representing the date or time as well as a format string.
print (time_obiject) # this very diffuct read format 
"""






"""
# here we can pass upto nine values to the tuple()
#(year, month, day, hour, minutes, second, #day of a week, #day of a year, dst)   dst << -1 or 0 for daylight saving time 
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # it accepts a tuple() representing of a reference time 
print (time_string)

# mktime will take a tuple representation of a time or a time obiject an converted to seconds since epic 
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) # it accepts a tuple() representing of a reference time 
print (time_string)
"""




'''