# Python Iterators
# An iterator is an object that contains values inside itself and gives one one item at a time.
# It uses __iter__() to start and __next__() to continue.
# Lists, tuples, dictionaries, and sets are iterable objects.

import datetime
import math
import json
from mymodule import person1
import platform
import mymodule as mx
import mymodule
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# This prints each letter of "banana" word.
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

# Iterate the characters of a string:
mystr = "banana"

for x in mystr:
    print(x)

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

# The __next__() method also allows you to do operations, and must return the next item in the sequence.


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# Python Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

# String
x = "Hello World!"

print(len(x))

# Tuple

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

# Dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(thisdict))

# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    x.move()

# Inheritance Class Polymorphism


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# Python Scope

# A variable is only available from inside the region it is created. This is called scope.

# Local Scope


def myfunc():
    x = 300
    print(x)


myfunc()

# Function inside Function


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()

# Global Scope

x = 300


def myfunc():
    print(x)


myfunc()

print(x)

# Naming Variables

x = 300


def myfunc():
    x = 200
    print(x)


myfunc()

print(x)

# Global Keyword


def myfunc():
    global x
    x = 300


myfunc()

print(x)

# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.


def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x


print(myfunc1())

# Python Modules

# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.


mymodule.greeting("Jonathan")


a = mymodule.person1["age"]
print(a)

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Renaming a Module
# You can create an alias when you import a module, by using the as keyword:


a = mx.person1["age"]
print(a)

# Built-in Modules

x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:


x = dir(platform)
print(x)

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.


def greeting(name):
    print("Hello, " + name)


person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

print(person1["age"])


# Python Datetime
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.


x = datetime.datetime.now()
print(x)

# When we execute the code from the example above the result will be:

# 2025-06-11 21:29:16.413649
# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.

# Here are a few examples, you will learn more about them later in this chapter:
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


x = datetime.datetime(2020, 5, 17)

print(x)


x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %C	Century	20
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%
# %G	ISO 8601 year	2018
# %u	ISO 8601 weekday (1-7)	1
# %V	ISO 8601 weeknumber (01-53)	01


# Python Math
# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


x = abs(-7.25)

print(x)


x = pow(4, 3)

print(x)

x = math.sqrt(64)

print(x)


x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # returns 2
print(y)  # returns 1


x = math.pi

print(x)

# Python JSON
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.


# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# You can convert Python objects of the following types, into JSON strings:

""" dict
list
tuple
string
int
float
True
False
None """


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


""" Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null """


x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))


# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:

# Example
# Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)


# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# Example
# Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))
# Order the Result
# The json.dumps() method has parameters to order the keys in the result:

# Example
# Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
