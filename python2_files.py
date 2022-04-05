
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






