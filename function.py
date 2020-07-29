# A function is a block of code which only runs when it is called. You can pass data, known
# as parameters, into a function. A function can return data as a result.

# Define a Python Function
def hello_world():
    print('Hello World!')


# call a function
hello_world()
# Hello World!


# Passing a single argument
def hello_friend(friend):
    print(f'Hello, {friend}!')


# call function passing in argument
hello_friend('Mosely')
hello_friend('Winnie')
# Hello, Mosely!
# Hello, Winnie!


# Passing a list as an argument
def hello_friends(names):
    for name in names:
        message = f'Hello, {name}!'
        print(message)


# call function passing in a list
hello_friends(['Winnie', 'Mosely', 'Bella', 'Mugsy'])
# Hello, Winnie!
# Hello, Mosely!
# Hello, Bella!
# Hello, Mugsy!


# Use a function to modify a list
def hello_friends(names):
    while names:
        name = names.pop()
        message = f'Hello, {name}!'
        print(message)


original = ['Winnie', 'Mosely', 'Bella', 'Mugsy']
print(original)
# ['Winnie', 'Mosely', 'Bella', 'Mugsy']

hello_friends(original)
# Hello, Mugsy!
# Hello, Bella!
# Hello, Mosely!
# Hello, Winnie!

print(original)
# []


#  Prevent a function from modifying a list
def hello_friends(names):
    while names:
        name = names.pop()
        message = f'Hello, {name}!'
        print(message)


original = ['Winnie', 'Mosely', 'Bella', 'Mugsy']
copy = original[:]
print(original)
# ['Winnie', 'Mosely', 'Bella', 'Mugsy']

hello_friends(copy)
# Hello, Mugsy!
# Hello, Bella!
# Hello, Mosely!
# Hello, Winnie!

print(original)
# ['Winnie', 'Mosely', 'Bella', 'Mugsy']


# Using positional arguments
def describe_car(make, model):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru', 'WRX')
# The Subaru WRX is a neat vehicle

describe_car('Tesla', 'Model 3')
# The Tesla Model 3 is a neat vehicle

describe_car('Tesla', 'Cybertruck')
# The Tesla Cybertruck is a neat vehicle


# Using keyword arguments
def describe_car(make, model):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru', 'WRX')
# The Subaru WRX is a neat vehicle

describe_car(make='Tesla', model='Model 3')
# The Tesla Model 3 is a neat vehicle

describe_car(model='Corvette', make='Chevy')
# The Chevy Corvette is a neat vehicle


# Using a default value
def describe_car(make, model='WRX'):
    print(f'The {make} {model} is a neat vehicle')


describe_car('Subaru')
# The Subaru WRX is a neat vehicle


# Using None to make an argument optional
def describe_car(make, model=None):
    if model:
        print(f'The {make} {model} is a neat vehicle')
    else:
        print(f'The {make} is a neat vehicle')


describe_car('Subaru')
# The Subaru is a neat vehicle

describe_car(model='Corvette', make='Chevy')
# The Chevy Corvette is a neat vehicle


# Function with an arbitrary number of arguments
def make_a_sandwich(type, *veggies):
    print(f'\nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggie}')


make_a_sandwich('Ham', 'Onions')
# Making a Ham Sandwich.
# It has these veggies:
# - Onions

make_a_sandwich('Roast Beef', 'Lettuce', 'Tomato')
# Making a Roast Beef Sandwich.
# It has these veggies:
# - Lettuce
# - Tomato

make_a_sandwich('Turkey', 'Lettuce', 'Tomato', 'Peppers')
# Making a Turkey Sandwich.
# It has these veggies:
# - Lettuce
# - Tomato
# - Peppers


# Collecting an arbitrary number of keyword arguments
def make_a_sandwich(type, **veggies):
    print(f'\nMaking a {type} Sandwich.')
    print('It has these veggies:')
    for veggie in veggies:
        print(f'- {veggies[veggie]}')


make_a_sandwich('Ham', one='Onions')
# Making a Ham Sandwich.
# It has these veggies:
# - Onions

make_a_sandwich('Roast Beef', one='Onions', two='Peppers')
# Making a Roast Beef Sandwich.
# It has these veggies:
# - Onions
# - Peppers

make_a_sandwich('Turkey', one='Olives', two='Spinach', three='Cucumbers')
# Making a Turkey Sandwich.
# It has these veggies:
# - Olives
# - Spinach
# - Cucumbers


# Returning a single value
def get_full_name(first, last):
    full_name = f'{first} {last}'
    return full_name.title()


comedian = get_full_name('ricky', 'gervais')
print(comedian)
# Ricky Gervais


# Returning a dictionary
def build_house(type, bedrooms):
    house = {'type': type, 'bedrooms': bedrooms}
    return house


house = build_house('Colonial', 3)
print(house)
# {'type': 'Colonial', 'bedrooms': 3}


# Returning a dictionary with optional values
def build_house(type, bedrooms, pool=None):
    house = {'type': type, 'bedrooms': bedrooms}
    if pool:
        house['pool'] = pool
    return house


house = build_house('Colonial', 3)
print(house)
# {'type': 'Colonial', 'bedrooms': 3}

house = build_house('Colonial', 2, 'No')
print(house)
# {'type': 'Colonial', 'bedrooms': 2, 'pool': 'No'}
