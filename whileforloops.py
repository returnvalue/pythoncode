# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.  A while loop
# statement in the Python Programming language repeatedly executes a target statement as long as a given condition is true.


# A simple program that counts to 3 is a great first example of the while statement.
count = 1
while count <= 3:
    print(count)
    count += 1
# 1
# 2
# 3


# You can break out of a while loop with the break keyword.
while True:
    word = input('Enter a string and I will print it backwards(type q to quit): ')
    if word == 'q':
        break
    print(word[::-1])
# Enter a string and I will print it backwards(type q to quit): Python
# nohtyP
# Enter a string and I will print it backwards(type q to quit): Wow it works!
# !skrow ti woW
# Enter a string and I will print it backwards(type q to quit): q


# Skip Ahead With continue
num = 0
while num <= 10:
    num += 1
    if num % 2 != 0:
        continue
    print(num)
# 2
# 4
# 6
# 8
# 10


# Using else With break
words = ['cat', 'rat', 'bat']
i = 0
while i < len(words):
    word = words[i]
    if len(word) == 4:
        print(f'{word} has 4 characters')
        break
    i += 1
else:
    print('No words have 4 characters')
# No words have 4 characters

# else not used here
words = ['cat', 'rat', 'bat', 'brat']
i = 0
while i < len(words):
    word = words[i]
    if len(word) == 4:
        print(f'{word} has 4 characters')
        break
    i += 1
else:
    print('No words have 4 characters')
# brat has 4 characters


# Multiple Conditions In A while Loop
color, number, count = 'red', 7, 0
while color == 'red' and number == 7 and count < 3:
    if count == 0:
        print('color is ', color)
    elif count == 1:
        print(number, ' is the number')
    else:
        print('while statement multiple conditions example')
    count += 1
# color is  red
# 7  is the number
# while statement multiple conditions example


# Nested while Loop
outer = 1
inner = 5
print('Outer|Inner')
while outer <= 4:
    while inner <= 8:
        print(outer, '---|---', inner)
        inner += 1
        outer += 1
# Outer|Inner
# 1 ---|--- 5
# 2 ---|--- 6
# 3 ---|--- 7
# 4 ---|--- 8


# while Loop User Input
number = 3
while True:
    what_number = input('What number is it? [type q to quit]:  ')
    if what_number == 'q':
        print('Thanks for guessing!')
        break
    if int(what_number) == number:
        print('You got it!')
        break
# What number is it? [type q to quit]:  1
# What number is it? [type q to quit]:  2
# What number is it? [type q to quit]:  3
# You got it!


# for loop through list
trees = ['Pine', 'Maple', 'Cedar']
for tree in trees:
    print(tree)
# Pine
# Maple
# Cedar


questions = ['Whats up?', 'How are you?', 'What time is it?']
for question in questions:
    print(question)
# Whats up?
# How are you?
# What time is it?


# for loop through tuple
boats = ('Row', 'Motor', 'Sail')
for boat in boats:
    print(boat + ' Boat')
# Row Boat
# Motor Boat
# Sail Boat


# for loop through string
for letter in 'Winnipesaukee':
    print(letter)
# W
# i
# n
# n
# i
# p
# e
# s
# a
# u
# k
# e
# e


# for loop through dictionary keys
forecast = {'Mon': 'Rainy', 'Tues': 'Partly Cloudy', 'Wed': 'Sunny', 'Thu': 'Windy', 'Fri': 'Warm', 'Sat': 'Hot',
            'Sun': 'Clear'}

for day in forecast:
    print(day)
# Mon
# Tues
# Wed
# Thu
# Fri
# Sat
# Sun


# for loop through dictionary values
forecast = {'Mon': 'Rainy', 'Tues': 'Partly Cloudy', 'Wed': 'Sunny', 'Thu': 'Windy', 'Fri': 'Warm', 'Sat': 'Hot',
            'Sun': 'Clear'}

for weather in forecast.values():
    print(weather)
# Rainy
# Partly Cloudy
# Sunny
# Windy
# Warm
# Hot
# Clear


# for loop through dictionary keys and values
forecast = {'Mon': 'Rainy', 'Tues': 'Partly Cloudy', 'Wed': 'Sunny', 'Thu': 'Windy', 'Fri': 'Warm', 'Sat': 'Hot',
            'Sun': 'Clear'}

for day, weather in forecast.items():
    print(day + ' will be ' + weather)
# Mon will be Rainy
# Tues will be Partly Cloudy
# Wed will be Sunny
# Thu will be Windy
# Fri will be Warm
# Sat will be Hot
# Sun will be Clear


# for loop with counter
str_nums = ['one', 'two', 'three', 'four', 'five']
for counter in range(5):
    print(counter, str_nums[counter])
# 0 one
# 1 two
# 2 three
# 3 four
# 4 five


# for loop with counter using enumerate
str_nums = ['one', 'two', 'three', 'four', 'five']
for counter, val in enumerate(str_nums):
    print(counter, val)
# 0 one
# 1 two
# 2 three
# 3 four
# 4 five


# break and continue statements With for Loops
for letter in 'Programming':
    if letter == 'a':
        print('Found "r", Breaking Out Of Loop Now')
        break
    print('Current Letter :', letter)
# Current Letter : P
# Current Letter : r
# Current Letter : o
# Current Letter : g
# Current Letter : r
# Found "r", Breaking Out Of Loop Now


for num in range(10):
    if num == 7:
        print('Seven is not so lucky')
        continue
    print(num)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# Seven is not so lucky
# 8
# 9


# Check break Use With else In for Loop
for letter in 'Programming':
    if letter == 'Z':
        print('Found "Z", Breaking Out Of Loop Now')
        break
    print('Current Letter :', letter)
else:
    print('Did Not Find "Z"')
# Current Letter : P
# Current Letter : r
# Current Letter : o
# Current Letter : g
# Current Letter : r
# Current Letter : a
# Current Letter : m
# Current Letter : m
# Current Letter : i
# Current Letter : n
# Current Letter : g
# Did Not Find "Z"


# nested for loop
nums = [1, 2, 3]
letters = ['xx', 'yy', 'zz']

for number in nums:
    print(number)
    for letter in letters:
        print(letter)
# 1
# xx
# yy
# zz
# 2
# xx
# yy
# zz
# 3
# xx
# yy
# zz


columns = [1, 2, 3]
rows = [1, 2, 3, 4]
for column in columns:
    if column == 1:
        print('      |', end='')
    print('column', column, '|', end='')
    if column == 3:
        print()
        for row in rows:
            print('row', row, f'| r{row}, c1  | r{row}, c2  | r{row}, c3  |')
#       |column 1 |column 2 |column 3 |
# row 1 | r1, c1  | r1, c2  | r1, c3  |
# row 2 | r2, c1  | r2, c2  | r2, c3  |
# row 3 | r3, c1  | r3, c2  | r3, c3  |
# row 4 | r4, c1  | r4, c2  | r4, c3  |


# while loop backwards
countdown = ['Blastoff!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
start = 10
while start >= 0:
    print(countdown[start])
    start -= 1
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Blastoff!


# for loop backwards
countdown = ['Blastoff!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for i in range(10, -1, -1):
    print(countdown[i])
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Blastoff!


# Loop Over Several Iterables At Once
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for letter, number in zip(letters, numbers):
    print(f'Letter: {letter}')
    print(f'Number: {number}')
    print('------------------')
# Letter: a
# Number: 0
# ------------------
# Letter: b
# Number: 1
# ------------------
# Letter: c
# Number: 2
# ------------------
