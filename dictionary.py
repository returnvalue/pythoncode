# A Python dictionary is a collection which is unordered, mutable, and indexed. In Python dictionaries
# are written with curly brackets, and they have keys and values.

# Making a dictionary
player_0 = {'level': 'novice', 'points': 7}

print(player_0['level'])
# novice

print(player_0['points'])
# 7


# Using the get() method to access a value
player_0 = {'level': 'novice'}
player_level = player_0.get('level')
player_points = player_0.get('points', 0)
print(player_level)
# novice

print(player_points)
# 0


# Dictionaries Inside Lists
# Start with an empty list.
profiles = []

# Make a new profile, and add them to the list.
new_profile = {
    'last': 'Diaz',
    'first': 'Guillermo',
    'profilename': 'gDiaz',
}
profiles.append(new_profile)

# Make another new profile, and add them as well.
new_profile = {
    'last': 'Rezende',
    'first': 'Pedro',
    'profilename': 'pRezende',
}
profiles.append(new_profile)

# Show all information about each profile.
for profile_dict in profiles:
    for k, v in profile_dict.items():
        print(f"{k}: {v}")
print("\n")
# last: Diaz
# first: Guillermo
# profilename: gDiaz
# last: Rezende
# first: Pedro
# profilename: pRezende

# Defining a list of dictionaries without using append()
profiles = [
    {
        'last': 'Diaz',
        'first': 'Guillermo',
        'profilename': 'eDiaz',
    },
    {
        'last': 'Rezende',
        'first': 'Pedro',
        'profilename': 'mRezende',
    },
]

# Show all information about each profile.
for profile_dict in profiles:
    for k, v in profile_dict.items():
        print(f"{k}: {v}")
print("\n")
# last: Diaz
# first: Guillermo
# profilename: eDiaz
# last: Rezende
# first: Pedro
# profilename: mRezende


# Adding a key-value pair
player_0 = {'level': 'novice', 'points': 7}
player_0['x'] = 0
player_0['y'] = 25
player_0['speed'] = 1.5

# The above code may also be written as a dictionary literal like so.
player_0 = {'level': 'novice', 'points': 7, 'x': 0, 'y': 25, 'speed': 1.5}

# Adding to an empty dictionary
player_0 = {}
player_0['level'] = 'novice'
player_0['points'] = 7

# Modifying values in a dictionary
# Change the player's level and point value.
player_0['level'] = 'intermediate'
player_0['points'] = 10
print(player_0)
# {'level': 'intermediate', 'points': 10}


# Removing key-value pairs
player_0 = {'level': 'novice', 'points': 7}

del player_0['points']
print(player_0)
# {'level': 'novice'}


# Storing lists in a dictionary
fav_games = {
    'Pedro': ['Outer Wilds', 'Disco Elysium'],
    'Sean': ['Baba Is You'],
    'Daniel': ['Sekiro', 'Star Wars Jedi'],
    'Guillermo': ['Control', 'Dragon Quest Builders 2'],
}

# Show each name and associated games
for name, games in fav_games.items():
    print(f"{name}: ")
    for game in games:
        print(f"- {game}")
# Pedro:
# - Outer Wilds
# - Disco Elysium
# Sean:
# - Baba Is You
# Daniel:
# - Sekiro
# - Star Wars Jedi
# Guillermo:
# - Control
# - Dragon Quest Builders 2

# Storing dictionaries in a dictionary
profiles = {
    'smcloughlin': {
        'first': 'Sean',
        'last': 'McLoughlin',
        'gender': 'male',
    },
    'prezende': {
        'first': 'Pedro',
        'last': 'Rezende',
        'gender': 'male',
    },
}
for profilename, profile_dict in profiles.items():
    print("\nUsername: " + profilename)
    full_name = profile_dict['first'] + " "
    full_name += profile_dict['last']
    gender = profile_dict['gender']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tgender: {gender.title()}")

# Username: smcloughlin
# 	Full name: Sean Mcloughlin
# 	gender: Male

# Username: prezende
# 	Full name: Pedro Rezende
# 	gender: Male


# Looping through all key-value pairs
# Store people's favorite games.
fav_games = {
    'George': 'Crash Bandicoot',
    'Alex': 'Super Smash Bros',
    'Sarah': 'Legend Of Zelda',
    'Allison': 'Pong',
}

# Loop over key and value
for name, game in fav_games.items():
    print(f"{name}: {game}")
# George: Crash Bandicoot
# Alex: Super Smash Bros
# Sarah: Legend Of Zelda
# Allison: Pong


# Looping through all the keys
for name in fav_games.keys():
    print(name)
# George
# Alex
# Sarah
# Allison

# Looping through all the values
for game in fav_games.values():
    print(game)
# Crash Bandicoot
# Super Smash Bros
# Legend Of Zelda
# Pong

# Looping through all the keys in reverse order
for name in sorted(fav_games.keys(), reverse=True):
    print(f"{name}: {fav_games[name]}")
# Sarah: Legend Of Zelda
# George: Crash Bandicoot
# Allison: Pong
# Alex: Super Smash Bros

# Checking The Length Of A Dictionary
num_responses = len(fav_games)
print(num_responses)
# 4


# Using a loop to create a dictionary
cubes = {}
for x in range(5):
    cubes[x] = x ** 3
print(cubes)
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# Using a dictionary comprehension
cubes = {x: x ** 3 for x in range(5)}
print(cubes)
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# Using zip() to make a dictionary
veggies = ['pepper', 'broccoli', 'spinach', 'potato']
fruits = ['apple', 'orange', 'peach', 'plum']
combos = {key: key_2 for key, key_2 in zip(veggies, fruits)}
print(combos)
# {'pepper': 'apple', 'broccoli': 'orange', 'spinach': 'peach', 'potato': 'plum'}

# To create a large number of dictionaries at once, you can use a loop like so.
players = []
# Make a thousand novice players, worth 3 points
# each. Have them all start in one row.
for player_num in range(1000):
    new_player = {}
    new_player['level'] = 'novice'
    new_player['points'] = 3
    new_player['x'] = 20 * player_num
    new_player['y'] = 0
    players.append(new_player)

# Show the list contains a thousand players.
num_players = len(players)

print("Number of players created:")
# Number of players created:

print(num_players)
# 1000
