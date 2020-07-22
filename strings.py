# Like many other popular programming languages, strings in Python are arrays of bytes representing
# unicode characters. However, Python does not have a character data type, a single character is
# simply a string with a length of 1. Square brackets [] can be used to access elements of the string.

# single or double qoutes to define a string
'A cool string'
"The second cool string"
''
" "

# using single and double quotes
'My friend is always using "Air Quotes" when she gets sarcastic'
"Python now has what is known as 'f strings' to make working with strings easier"
"It's fun to use strings in Python"

# Using str() To Create A String
one = str(712)
print(type(one))
# <class 'str'>

two = str(3.14)
print(type(two))
# <class 'str'>

three = str(True)
print(type(three))
# <class 'str'>

four = str(['list', 'of', 'things'])
print(type(four))
# <class 'str'>

five = str({'dictionary': 17})
print(type(five))
# <class 'str'>

# Concatenate Strings Using +
result = 'Check out ' + 'this Python String!'
print(result)
# Check out this Python String!

str_var1 = 'Check out '
str_var2 = 'this Python String!!'
print(str_var1 + str_var2)
# Check out this Python String!!

# Python will automatically concatenate for you with no use of the + operator.
bigmix = 'This is ' "a string " '''added together'''
print(bigmix)
# This is a string added together

# Multiplying Strings
two_of_two = 'two ' * 2
print(two_of_two)
# two two

three_of_three = 'three ' * 3
print(three_of_three)
# three three three

five_of_five = 'five ' * 5
print(five_of_five)
# five five five five five

# Python String Format
string_variable = 'Python'
print('{} is the best programming language'.format(string_variable))
# Python is the best programming language

first = '1st variable'
second = '2nd variable'
third = '3rd variable'
print('This is the {}, {}, and {}'.format(first, second, third))
# This is the 1st variable, 2nd variable, and 3rd variable

# use of f-strings:
first = '1st variable'
second = '2nd variable'
third = '3rd variable'
print(f'This is the {first}, {second}, and {third}')
# This is the 1st variable, 2nd variable, and 3rd variable

# Single quotes using the escape character
'My friend is always using \'Air Quotes\' when she gets sarcastic'
'Python now has what is known as \'f strings\' to make working with strings easier'
'It\'s fun to use strings in Python'

# Double quotes using the escape character
"My friend is always using \"Air Quotes\" when she gets sarcastic"
"Python now has what is known as \"f strings\" to make working with strings easier"
"Its fun to use strings in Python"

# example of a raw string in Python:
print(r'Some common escape characters are \', \", \t, \n, and \\')
# Some common escape characters are \', \", \t, \n, and \\

# Triple Quoted Strings
print('''This string

has some line breaks

in it''')
# This string
#
# has some line breaks
#
# in it

# Single and Double Quotes inside Triple Quotes
print('''I don't like your overused "Air Quotes"''')


# I don't like your overused "Air Quotes"

# docstrings
def str_to_title(the_string):
    '''Accepts a string as input, and returns the title case of the string'''
    return the_string.title()


# The in operator
print('I' in 'Team')
# False

print('I' in 'Incredible')
# True

# The not in operator
print('I' not in 'Team')
# True

print('I' not in 'Incredible')
# False


# The .find() function
print('Team'.find('I'))
# -1

print('Team'.find('m'))
# 3


# Case Methods
the_str = 'Cool Fun String'

print(the_str.lower())
# cool fun string

the_str = 'Cool Fun String'

print(the_str.swapcase())
# cOOL fUN sTRING

the_str = 'cool fun string'

print(the_str.title())
# Cool Fun String

the_str = 'Cool Fun String'

print(the_str.upper())
# COOL FUN STRING

the_str = 'Cool Fun String'

print(the_str.islower())
# False

the_str = 'Cool Fun String'

print(the_str.istitle())
# True

the_str = 'Cool Fun String'

print(the_str.isupper())
# False

the_str = 'Cool Fun String'

print(the_str.capitalize())
# Cool fun string

# Slice Strings
the_str = 'This string has five words'

print(the_str.index('f'))
# 16

# the_str = 'Stringify'

print(the_str.index('g'))
# 5

the_str = 'Stringify'
print(the_str[0])
# S

the_str = 'Stringify'
print(the_str[3])
# i

the_str = 'Stringify'
print(the_str[-1])
# y

the_str = 'Stringify'
print(the_str[0:6])
# String

the_str = 'Stringify'
print(the_str[0:3])
# Str

the_str = 'Stringify'
print(the_str[6:])
# ify

# built-in len() function.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(len(alphabet))
# 26

# Substring Substitution Using replace()
old = 'Out with the new, in with the new'
new = old.replace('new', 'old')
print(new)
# Out with the old, in with the old

old = 'Out with the new, in with the new'
new = old.replace('new', 'old', 1)
print(new)
# Out with the old, in with the new

# .split() example
the_str = 'Just A String'
print(the_str.split())
# ['Just', 'A', 'String']

# .join() example
a_list = ['Just', 'A', 'String']
print(' '.join(a_list))
# Just A String

a_list = ['Just', 'A', 'String']
print(' 😃 '.join(a_list))
# Just 😃 A 😃 String

# .count() example
the_str = 'Just another test string'
print(the_str.count('test'))
# 1

the_str = 'Just another test string'
print(the_str.count('s'))
# 3

the_str = 'Just another test string'
print(the_str.count('e'))
# 2

# .startswith() and .endswith() methods.
the_str = 'Just another test string'
print(the_str.startswith('Just'))
# True

the_str = 'Just another test string'
print(the_str.startswith('Hacking'))
# False

the_str = 'Just another test string'
print(the_str.endswith('g'))
# True

the_str = 'Just another test string'
print(the_str.endswith('n'))
# False

# using tabs
one = 'Python String'
two = '\tPython String'
three = '\t\tPython String'
print(one, two, three)
# Python String 	Python String 		Python String

one = 'Python String\n'
two = '\tPython String\n'
three = '\t\tPython String'
print(one, two, three)
# Python String
#  	Python String
#  		Python String

# Tabs To Spaces With expandtabs()
the_str = '\tStrawberry Blueberry Jam\t'
print(the_str.expandtabs(4))
#     Strawberry Blueberry Jam

# Using strip() rstrip() and lstrip()
custom = 'badword This is a nice string badword'
print(custom.strip('badword'))
#  This is a nice string

# Aligning Strings
the_str = 'Strawberry Blueberry Jam'
print(the_str.center(34))
print(the_str.ljust(34))
print(the_str.rjust(34))
#      Strawberry Blueberry Jam
# Strawberry Blueberry Jam
#           Strawberry Blueberry Jam

the_str = 'Strawberry Blueberry Jam'
print(the_str.center(34, '🍓'))
print(the_str.ljust(34, '🌱'))
print(the_str.rjust(34, '🌱'))
# 🍓🍓🍓🍓🍓Strawberry Blueberry Jam🍓🍓🍓🍓🍓
# Strawberry Blueberry Jam🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
# 🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱Strawberry Blueberry Jam
