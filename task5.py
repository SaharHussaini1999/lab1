# Python RegEX
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a buit-in package calledd re, which can be used to work with Regular Expressions.
# Import the re module:

import re

# RegEx in Python
# When you have imported the re module, you can start using regular expressions:

import re

# Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:
"""
Function    Description

findall     Returns a list containing all matches
search      Returns a Match object if there is a match anywhere in the string
split       Returns a list where the string has been split at each match
sub         Replaces one or many matches with a string
"""

# Metacharacters
# Metacharacters are characters with a special meaning:


# [] A set of characters
txt = "The rain in Spain"

# Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

# \	Signals a special sequence (can also be used to escape special characters)

txt = "That will be 59 dollars"

# Find all digit characters:

x = re.findall("\d", txt)
print(x)

# . Any character (except newline character)
txt = "hello planet"

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

# ^	Starts with
txt = "hello planet"

# Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

# $ Ends with
txt = "hello planet"

# Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

# * Zero or more occurrences
txt = "hello planet"

# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)
# + One or more occurrences

txt = "hello planet"

# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)
# ? Zero or one occurrences
txt = "hello planet"

# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

# This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
# {} Exactly the specified number of occurrences

# | Either or
txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# () Capture and group

# Flags
# You can add flags to the pattern when using regular expressions.
"""
Flag        Shorthand       Description
re.ASCII	re.A	Returns only ASCII matches
"""

txt = "Åland"

# Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))

# Without the flag, the example would return all character:
print(re.findall("\w", txt))


# Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))

"""
Flag        Shorthand       Description
re.DEBUG		Returns debug information
"""

txt = "The rain in Spain"

# Use a case-insensitive search when finding a match for Spain in the text:

print(re.findall("spain", txt, re.DEBUG))

"""
Flag        Shorthand       Description
re.DOTALL	re.S	        Makes the . character match all characters (including newline character)
"""
txt = """Hi
my
name
is
Sally"""

# Search for a sequence that starts with "me", followed by one character, even a newline character, and continues with "is":
print(re.findall("me.is", txt, re.DOTALL))

# This example would return no match without the re.DOTALL flag:
print(re.findall("me.is", txt))


# Same result with the shorthand re.S flag:
print(re.findall("me.is", txt, re.S))
"""
Flag        Shorthand       Description
re.IGNORECASE	re.I	    Case-insensitive matching
"""
txt = "The rain in Spain"

# Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.IGNORECASE))


# Same result using the shorthand re.I flag:
print(re.findall("spain", txt, re.I))
"""
Flag             Shorthand       Description
re.MULTILINE	 re.M	    Returns only matches at the beginning of each line
"""

txt = """There
aint much
rain in 
Spain"""

# Search for the sequence "ain", at the beginning of a line:
print(re.findall("^ain", txt, re.MULTILINE))

# This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning of the text:
print(re.findall("^ain", txt))


# Same result with the shorthand re.M flag:
print(re.findall("^ain", txt, re.M))
"""
Flag        Shorthand           Description
re.NOFLAG	Specifies that no flag is set for this pattern


Flag        Shorthand           Description
re.UNICODE	re.U	            Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches
"""

txt = "Åland"

# Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE))


# Same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U))
"""
Flag        Shorthand           Description
re.VERBOSE	re.X	            Allows whitespaces and comments inside patterns. Makes the pattern more readable
"""
text = "The rain in Spain falls mainly on the plain"

# Find and return words that contains the phrase "ain":

pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""

print(re.findall(pattern, text, re.VERBOSE))

# The example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, text))


# Same result with the shorthand re.X flag:
print(re.findall(pattern, text, re.X))

# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
"""
Character   Description
\A      	Returns a match if the specified characters are at the beginning of the string
"""

txt = "The rain in Spain"

# Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")
"""
Character   Description
\b	        Returns a match where the specified characters are at the beginning or at the end of a word
"""
txt = "The rain in Spain"

# Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
txt = "The rain in Spain"

# Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
"""
Character   Description
\B	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
"""

txt = "The rain in Spain"

# Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
txt = "The rain in Spain"

# Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
"""
Character   Description
\d	        Returns a match where the string contains digits (numbers from 0-9)"""
txt = "The rain in Spain"

# Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
"""
Character   Description
\D	        Returns a match where the string DOES NOT contain digits
"""
txt = "The rain in Spain"

# Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

"""
Character   Description
\s	        Returns a match where the string contains a white space character
"""
txt = "The rain in Spain"

# Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
"""
Character   Description
\S	        Returns a match where the string DOES NOT contain a white space character
"""
txt = "The rain in Spain"

# Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

"""
Character   Description
\w	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
"""
txt = "The rain in Spain"

# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
"""
Character   Description
\W	        Returns a match where the string DOES NOT contain any word characters
"""

txt = "The rain in Spain"

# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

"""
Character   Description
\Z	        Returns a match if the specified characters are at the end of the string
"""

txt = "The rain in Spain"

# Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")

# Sets
# A set is a set of characters inside a pair of squar brackets [] with a special meaning:

""" 
Set	Description	Try it
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
 """

# The findall() Function
# The findall() function returns a list containing all matches.


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# The list contains the matches in the order they are found.

# If no matches are found, an empty list is returned:

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# The search() Function

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# The sub() Function

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


# Match Object
# A Match Object is an object containing information about the search and the result.


txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object


# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
