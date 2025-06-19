# File Handling
# it means we open other file by python.
# Python has several functions for creatnig, readnig and deleting files.
# the key function for working with files in python is the open() function.

# r = read the file
# w = write the file and delet all texts that are exist in the file.
# a = append at the ind of file.
# x = creat file

#In addition you can specify if the file should be handled as binary or text mode
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#Syntax = To open a file for reading it is enough to specify the name of the file:
# exmple:f = open("demofile.txt") these two are the samef = open("demofile.txt", "rt")


# Python File Open
# for opening the file use open().
#Example
f = open("demofile.txt", "r")

print(f.read())

# Open a file on a different location:

# f = open("D:\\myfiles\welcome.txt", "r")

# print(f.read())   ????

#Using the with statement
# when we use with statement it does not to use close() the file close after reading.
with open("demofile.txt", "r") as f:
    print(f.read())


#Close Files
#Close the file when you are finished with it:
# If we do not close maybe takes an error.
f = open("demofile.txt", "r")

print(f.readline())

f.close()


#Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
#Example=Return the 5 first characters of the file:
with open("demofile.txt", "r") as f:
  print(f.read(5))#Hello

#Read Lines
#You can return one line by using the readline() method
#Example=Read one line of the file
with open("demofile.txt") as f:
  print(f.readline())#Hello! Welcome to demofile.txt

#By calling readline() two times, you can read the two first lines
#Example= Read two lines of the file
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())  
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
 

#Use looping
#By looping through the lines of the file, you can read the whole file, line by line
#Example=Loop through the file line by line
with open("demofile.txt") as f:
  for x in f:
    print(x)
'''Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!'''


#Python File Write
#Write to an Existing File
#To write to an existing file, you must add a parameter to the open() function:
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

#Example=Open the file "demofile.txt" and append content to the file:
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

#Overwrite Existing Content
#To overwrite the existing content to the file, use the w parameter
#Example=Open the file "demofile.txt" and overwrite the content.
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
#Note: the "w" method will overwrite the entire file.
with open("demofile.txt") as f:
  print(f.read())#Woops! I have deleted the content!


#Create a New File
#To create a new file in Python, use the open() method, with one of the following parameters.
#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists

#Example= Create a new file called "myfile.txt":
#This will create a new file:
f = open("myfile.txt", "x")
# Note: If the file already exist, an error will be raised.

#Python Delete File
#To delete a file, you must import the OS module, and run its os.remove() function:
#Example=Remove the file "demofile.txt"
import os
os.remove("demofile.txt")

#Check if File exist:
#To avoid getting an error, you might want to check if the file exists before you try to delete it:
#Example=Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#Delete Folder
#To delete an entire folder, use the os.rmdir() method 
# Example=Remove the folder "myfolder"
import os
os.rmdir("myfolder")
#Note: You can only remove empty folders.


 
