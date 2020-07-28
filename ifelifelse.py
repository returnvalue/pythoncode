# A program's control flow is the order in which the program's code executes. The control flow of
# a Python program is regulated by conditional statements, loops, and function calls. Raising
# and handling exceptions also affects control flow

# Checking for equality
language = 'python'
print(language == 'python')
# True

# Checking for equality
language = 'JavaScript'
print(language == 'python')
# False

# Ignoring case when making a comparison
sandwich = 'Ham'
print(sandwich.lower() == 'ham')
# True

# Checking for inequality
vegetable = 'potato'
print(vegetable != 'potahto')
# True

# Basic if statement
color = 'Green'
if color == 'Green':
    print('Go!')
# Go!

# if-else statement
color = 'Orange'
if color == 'Green':
    print('Go!')
else:
    print('Don\'t Go!')
# Don't Go!

# if-elif-else statement
color = 'Green'
if color == 'Red':
    takeaction = 'Stop'
elif color == 'Yellow':
    takeaction = 'Slow Down'
elif color == 'Green':
    takeaction = 'Go'
else:
    takeaction = 'Maintain current state'
print(f'You need to {takeaction}.')
# You need to Go.

# Check if a value is not included in a list
foods = ['Snickers', 'Kit Kat', 'Butterfinger']
vegetable = 'Broccoli'
if vegetable not in foods:
    print("Eat some vegetables!")
# Eat some vegetables!

# Test whether a list is empty
cats = []
if cats:
    for cat in cats:
        print(f"Cat: {cat.title()}")
else:
    print("Thank God we have no cats!")
# Thank God we have no cats!

# Conditional tests with lists
programs = ['Photoshop', 'Illustrator', 'InDesign', 'Animate', 'Acrobat']
using = input('What program are you using? ')

if using in programs:
    print('That program is made by Adobe')
else:
    print('That is not an Adobe product')
# What program are you using? Word
# That is not an Adobe product

# A basic input example
fruit = input("What is your favorite fruit? ")
print(f"{fruit} is a great fruit!")
# What is your favorite fruit? Tomato
# Tomato is a great fruit!

# Getting numerical input using int()
favnum = input("What is your favorite number? ")
favnum = int(favnum)
if favnum == 7:
    print(f"{favnum} is also my favorite!")
else:
    print(f"{favnum} is a good choice!")
# What is your favorite number? 7
# 7 is also my favorite!

# Accepting numerical input via float()
pi = input("What is the value of pi? ")
pi = float(pi)
print(type(pi))
# What is the value of pi? 3.141592653589793238
# <class 'float'>

# Testing equality and inequality
num = 17
num == 17
# True

num != 17
# False

# Comparison operators
num = 250
num < 777
# True

num <= 777
# True

num > 777
# False

num >= 777
# False

# Using and to check multiple conditions
num_0 = 12
num_1 = 8
res = num_0 >= 11 and num_1 >= 11
print(res)
# False

num_1 = 23
res = num_0 >= 11 and num_1 >= 11
print(res)
# True

# Using or to check multiple conditions
num_0 = 12
num_1 = 8
res = num_0 >= 11 or num_1 >= 11
print(res)
# True

num_1 = 7
res = num_0 >= 15 or num_1 >= 14
print(res)
# False

# Basic Boolean values
subscription_active = True
is_cancelled = False

# Using if statements in loops
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print(f'iteration {i} fizzbuzz!')
    elif i % 3 == 0:
        print(f'iteration {i} fizz!')
    elif i % 5 == 0:
        print(f'iteration {i} buzz!')
    else:
        print(f'--none on iteration {i}--')
# --none on iteration 1--
# --none on iteration 2--
# iteration 3 fizz!
# --none on iteration 4--
# iteration 5 buzz!
# iteration 6 fizz!
# --none on iteration 7--
# --none on iteration 8--
# iteration 9 fizz!
# iteration 10 buzz!
# --none on iteration 11--
# iteration 12 fizz!
# --none on iteration 13--
# --none on iteration 14--
# iteration 15 fizzbuzz!

i = 1
while i < 16:
    if i % 3 == 0 and i % 5 == 0:
        print(f'iteration {i} fizzbuzz!')
    elif i % 3 == 0:
        print(f'iteration {i} fizz!')
    elif i % 5 == 0:
        print(f'iteration {i} buzz!')
    else:
        print(f'--none on iteration {i}--')
    i = i + 1
# --none on iteration 1--
# --none on iteration 2--
# iteration 3 fizz!
# --none on iteration 4--
# iteration 5 buzz!
# iteration 6 fizz!
# --none on iteration 7--
# --none on iteration 8--
# iteration 9 fizz!
# iteration 10 buzz!
# --none on iteration 11--
# iteration 12 fizz!
# --none on iteration 13--
# --none on iteration 14--
# iteration 15 fizzbuzz!

# Guessing A Secret Word
prompt = "Guess the secret word "
secret = ""
while secret != 'swordfish':
    secret = input(prompt)
    if secret != 'swordfish':
        print(f'{secret} is not the secret word')
    else:
        print('swordfish is the secret word!')
# Guess the secret word splish
# splish is not the secret word
# Guess the secret word splash
# splash is not the secret word
# Guess the secret word swordfish
# swordfish is the secret word!

# Using A Flag
# We can rewrite the word guessing game using a flag like so.
prompt = "Guess the secret word "
active = True
while active:
    secret = input(prompt)
    if secret != 'swordfish':
        print(f'{secret} is not the secret word')
    else:
        print('swordfish is the secret word!')
        active = False
# Guess the secret word hip
# splish is not the secret word
# Guess the secret word hop
# splash is not the secret word
# Guess the secret word swordfish
# swordfish is the secret word!

# Exit a loop with break
prompt = "What are your favorite colors? "
prompt += "Enter 'q' to quit. "
while True:
    color = input(prompt)
    if color == 'q':
        print("Thanks for sharing your colors!")
        break
    else:
        print(f"{color} is a great color!")
# What are your favorite colors? Enter 'q' to quit. red
# red is a great color!
# What are your favorite colors? Enter 'q' to quit. white
# white is a great color!
# What are your favorite colors? Enter 'q' to quit. blue
# blue is a great color!
# What are your favorite colors? Enter 'q' to quit. q
# Thanks for sharing your colors!

# Using continue in a loop
already_watched = ['Top Gun', 'Star Wars', 'Lord Of The Rings']
prompt = "Choose a movie to watch. "
prompt += "Enter 'q' to quit. "
movies = []
while True:
    movie = input(prompt)
    if movie == 'q':
        break
    elif movie in already_watched:
        print(f"I already saw {movie}")
        continue
    else:
        movies.append(movie)
    print("Movies to watch:")
    for movie in movies:
        print(movie)
# Choose a movie to watch. Enter 'q' to quit. Top Gun
# I already saw Top Gun
# Choose a movie to watch. Enter 'q' to quit. Rambo
# Movies to watch:
# Rambo
# Choose a movie to watch. Enter 'q' to quit. Star Wars
# I already saw Star Wars
# Choose a movie to watch. Enter 'q' to quit. Spider Man
# Movies to watch:
# Rambo
# Spider Man
# Choose a movie to watch. Enter 'q' to quit. q

# Removing all duplicates from a list of programs
programs = ['Photoshop', 'Illustrator', 'InDesign', 'Animate', 'Illustrator', 'Acrobat', 'Illustrator']
print(programs)
while 'Illustrator' in programs:
    programs.remove('Illustrator')
print(programs)
# ['Photoshop', 'Illustrator', 'InDesign', 'Animate', 'Illustrator', 'Acrobat', 'Illustrator']
# ['Photoshop', 'InDesign', 'Animate', 'Acrobat']
