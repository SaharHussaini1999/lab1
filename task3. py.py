# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

def my_func():
    print("Hell from a function")


my_func()


def my_function(name):
    print("My name is " + name)


my_function('Tamana')
my_function('Sahar')
my_function('Ahmad Ali')

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
# If the number of arguments is unknown, add a * before the parameter name:


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def child_names(child3, child2, child1):
    print("There are people from different ages: " + child3 +
          " 8 years old. " + child2 + " 12 years old. " + child1 + " 20 years old.")


# Arbitrary Arguments are often shortened to *args in Python documentations.
child_names(child2='Emil', child1='Tobias', child3='Linus')


# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

def my_func(**kwargs):
    print("Her last name is " + kwargs["lname"])


my_func(fname="Tamana", lname="Alizada")

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

# Default Parameter Value


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_list_func(foods):
    for food in foods:
        print(food)


foods = ["apple", "banana", "cherry"]
my_list_func(foods)

# Return values


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(4))


def my_func(name="Tamana"):
    print("My name is " + name)


my_func("Sahar")
my_func()

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example


def myfunction():
    pass


# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

# To specify that a function can have only positional arguments, add , / after the arguments:

# Example
# this function should be called like a positional argument. It means this is not allowed using keyword and arguments my_function(x = 3) false
def my_function(x, /):
    print(x)


my_function(3)


# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

# Example
def my_function(x):
    print(x)


my_function(x=3)

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

# Example


def my_function(*, x):
    print(x)


my_function(x=3)


# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:

# Example
def my_function(x):
    print(x)


my_function(3)

""" This will for sure give you error
  def my_function(*, x):
  print(x)

  my_function(3)
 """


# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

# Example


def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)

print("")


def factorial(k):
    if (k > 1):
        return k * factorial(k - 1)
    else:
        return 1


print(factorial(5))


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        """ print(result)
        print(k)
        print("") """
    else:
        result = 0
    print(result)
    return result


print("Recursion Example Results:")
tri_recursion(6)


# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
def myLambdaFunc(a): return a + 10


print(myLambdaFunc(32))
def x(a, b): return a * b


print(x(5, 6))
def x(a, b, c): return a + b + c


print(x(5, 6, 2))


def myFunc(n):
    return lambda a: a * n


x = myFunc(2)
print(x(11))
x = myFunc(3)
print(x(44))
# Or, use the same function definition to make a function that always triples the number you send in:z

# Arrays:
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

cars = ['Ford', 'Volvo', 'BMW']
x = cars[0]
print(x)

cars[0] = "Toyota"

x = len(cars)

for x in cars:
    print(x)

cars.append("Honda")
cars.pop(1)
cars.remove("Volvo")
# Note: The list's remove() method only removes the first occurrence of the specified value.
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# OOP
# In OOP, you create objects. Each object can store data and have functions that work with that data.

# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code
# Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.

# What are Classes and Objects?
# Classes and objects are the two core concepts in object-oriented programming.

# A class defines what an object should look like, and an object is created based on that class. For example:

# Class	Objects
# Fruit	Apple, Banana, Mango
# Car	Volvo, Audi, Toyota
# When you create an object from a class, it inherits all the variables and functions defined inside that class.


# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()

# modify object properties
p1.age = 40

del p1.age

del p1


class Person:
    pass

# Python Inheritance
# Parent class
# Child class


# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


x = Person("John", "Doe")
x.printname()


# Child class
class Student(Person):
    pass
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


x = Student("Mike", "Olsen")
x.printname()


""" class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc.


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) """


# Add Properties
# Add a property called graduationyear to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

# Add a year parameter, and pass the correct year when creating objects:


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)


# Add a method called welcome to the Student class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)
