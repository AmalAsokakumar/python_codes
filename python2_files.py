
#                                                               moving files using python 
# error occured and i am not able to figure it out.
'''
import os                           # normaly included in python lib


source = "/Users/amalasokakumar/Desktop/folder/1.txt "
destination = "/Users/amalasokakumar/Desktop/"

print (" a file is ready to move ")

#if os.path.exists (source):
    #print ("exist")

try:
    if os.path.exists(destination):
        print ("file already exist")
        os.replace(source,destination)

    else :
        #os.replace(source,destination)
        print("{} was moved".format(source))
except FileNotFoundError as e:
    print ("file not found \t {}".format(e))
'''





'''
import os 

#os.move("/Users/amalasokakumar/Desktop/new.txt", "/Users/amalasokakumar/Desktop")
#os.copy("/Users/amalasokakumar/Desktop/new.txt", "/Users/amalasokakumar/Desktop")
pwd = os.getcwd()                                                                               #os.getcwd()   to print current workin directory 
print (pwd)
os.chdir ((".."))
print (os.getcwd())
os.chdir("/Users/amalasokakumar/Desktop/folder")
print (os.getcwd())

#os.mkdir("/Users/amalasokakumar/Desktop/folder/test",(700))                                     #to create a new directory 
print (os.listdir(os.getcwd()))                                                                  #to list all the files in the directorty 



name = os.getlogin()                                                                             #log in as who 
print (name)
print (os.curdir)
print (os.getcwd())


import os

try:
    path = "/Users/amalasokakumar/Desktop/2.txt"
    os.remove(path)                                                                             # i can easly remove a file using this command 
except FileNotFoundError as e:
    print ("file not found \n {}".format(e))

'''
#https://www.geeksforgeeks.org/os-module-python-examples/         referance link 


'''

os.remove ("path")                                      #to delete a file value
os.rmdir ("path")                                       #to remove an empty directory

import shutil

shutil.rmtree ("path")                                  #to remove directort along with its files 

'''






#           ----------------------------------------------------------------modules ----------------------------------------------------------------
#                                                  a file containing pythone code. May containe functions, classes, etc 
#                                               used with modular programming, whic is to seperate programme into parts







































# ----------------------------------------------------------------     multithreading ------------------------------------------------------------------------------------

# 5:39/12:00:
#                                                                    thread >>>
#                                                                               a flow of execution, like a seperate order of instructions. 
#                                                                               However each thread takes a turn running to achieve concurency. 
#                                                                               GIL >>> (global interceptor lock) 
#                                                                               allows only one thread to hold the control of the python interpetor at any one time 

#                                                                   cpu bound >>
#                                                                               program/task spends most of it's time waiting for internal events (cpu intensive) 
#                                                                               use multi processing 


#                                                                   io bound  >>
#                                                                               program/task spends most of it's time waiting for external events 
#                                                                               (user input, web scraping) use multithreading 

'''
import threading
import time 


# print (time.ctime(time.time())) # print todays time and date 
# to count number of threads that are currentl running in background when we run the programm, we have one that is in chargeof 


# print (threading.active_count())
# print (threading.enumerate()) 


# Return a list of all Thread objects currently alive. The list includes daemonic threads, dummy thread objects created by current_thread(), and the main thread. It excludes terminated threads and threads that have not yet been started.

#  multi threading can be used to programme quiz game
#   in which a thread is incharge for the uset input while another thread is incharge for starting the countdown process 
#   hence we will have 2 threads running concurrently, if we have n number of threads they can all run concurrently they all takes turns while one of them is idel.





def eat_breakfast():
    time.sleep(3)
    print ("you eat breakfast ")


def drink_coffey():
    time.sleep(4)
    print ("You drink coffey")

def study ():
    time.sleep(5)
    print ("You finish study ")


# lets call all this functions using main thread
""" 
eat_breakfast()
drink_coffey()
study()
"""
# in here these 3 tasks are completed in sequential manner, its second task begins after the completion of first task and so on
# here we have a single thread incharge of the functions 



# now we can as 3 threads in which each one is incharge of a single fn and the main programe running in background that will complete  the programme by main thread 

# multi threading 
x = threading.Thread(target = eat_breakfast, args = ())
x.start()

y = threading.Thread(target = drink_coffey, args = ())
y.start()

z = threading.Thread(target = study, args = ())

"""
z.start()


x.join()  # now main thread have to wait till x thread is complete to continue (main threads) it's instructions sets 

y.join()
z.join()
"""
# now the main thread have to waite till all the threads to synchronize and join then only can it move on with the rest of the it's own instruction set 
print (threading.active_count())
print (threading.enumerate())
print (time.perf_counter())  # how much time the main thread using to complete the main program
'''






















































# time : 5:53/12:00
# 
# 
# 
# python 
# deamon thread 
