# Comprehensions in Python provide us with a short and concise way to
# construct new sequences (such as lists, set, dictionary etc.) using
# sequences which have been already defined.

# Simple List Comprehension
# for version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = []
for number in numbers:
    my_list.append(number)
print(my_list)
# [1, 2, 3, 4, 5, 6, 7]

# comprehension version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = [number for number in numbers]
print(my_list)
# [1, 2, 3, 4, 5, 6, 7]


# Taking An Action On Each Item
# for version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = []
for number in numbers:
    my_list.append(number * number)
print(my_list)
# [1, 4, 9, 16, 25, 36, 49]

# comprehension version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = [number * number for number in numbers]
print(my_list)
# [1, 4, 9, 16, 25, 36, 49]

# lambda version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = map(lambda number: number * number, numbers)
print(list(my_list))
# [1, 4, 9, 16, 25, 36, 49]


# Comprehension If
# for version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = []
for number in numbers:
    if number % 2 == 0:
        my_list.append(number * number)
print(my_list)
# [4, 16, 36]

# comprehension version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = [number * number for number in numbers if number % 2 == 0]
print(my_list)
# [4, 16, 36]


# Comprehension If Else
# for version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = []
for number in numbers:
    if number % 2 == 0:
        my_list.append(number)
    else:
        my_list.append(number * number)
print(my_list)
# [1, 2, 9, 4, 25, 6, 49]

# comprehension version
numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = [number if number % 2 == 0 else number * number for number in numbers]
print(my_list)
# [1, 2, 9, 4, 25, 6, 49]


# Comprehension Nested
# for version
my_list = []
for letter in 'abc':
    for number in range(1, 4):
        my_list.append((letter, number))
print(my_list)
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

# comprehension version
my_list = [(letter, number) for letter in 'abc' for number in range(1, 4)]
print(my_list)
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]


# Comprehensions Dictionary
# for version
colors = ['Red', 'Green', 'Orange']
veggies = ['Pepper', 'Onion', 'Squash']

my_dict = {}
for color, veggie in zip(colors, veggies):
    my_dict[color] = veggie
print(my_dict)
# {'Red': 'Pepper', 'Green': 'Onion', 'Orange': 'Squash'}

# comprehension version
colors = ['Red', 'Green', 'Orange']
veggies = ['Pepper', 'Onion', 'Squash']

my_dict = {color: veggie for color, veggie in zip(colors, veggies)}
print(my_dict)
# {'Red': 'Pepper', 'Green': 'Onion', 'Orange': 'Squash'}


# Dict Comprehension With If
# for version
colors = ['Red', 'Green', 'Orange']
veggies = ['Pepper', 'Onion', 'Squash']

my_dict = {}
for color, veggie in zip(colors, veggies):
    if color != 'Orange':
        my_dict[color] = veggie
print(my_dict)
# {'Red': 'Pepper', 'Green': 'Onion'}

# comprehension version
colors = ['Red', 'Green', 'Orange']
veggies = ['Pepper', 'Onion', 'Squash']

my_dict = {color: veggie for color, veggie in zip(colors, veggies) if color != 'Orange'}
print(my_dict)
# {'Red': 'Pepper', 'Green': 'Onion'}


# Comprehension Set
# for version
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
my_set = set()
for number in numbers:
    my_set.add(number)
print(my_set)
# {1, 2, 3, 4, 5}

# comprehension version
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
my_set = {number for number in numbers}
print(my_set)
# {1, 2, 3, 4, 5}
