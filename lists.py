# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
# Each element or value that is inside of a list is called an item.  They enable you to keep data
# together that belongs together, condense your code, and perform the same methods and operations
# on multiple values at once.

# ---------------------------------------------------------------------------------------- #
# define an empty list
empty_list = []

# ---------------------------------------------------------------------------------------- #
# individual elements in the list are separated by commas
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']

print(veggies)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']

# ---------------------------------------------------------------------------------------- #
# lists can hold all types
many_types = [7, 'letter', True, ['Kale', 'Cabbage'], {'Garlic': 2, 'Okra': 1, 'Carrot': 5}]
for item in many_types:
    print(type(item))
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# <class 'list'>
# <class 'dict'>

# ---------------------------------------------------------------------------------------- #
# using .count() method
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
lettuce = veggies.count('Lettuce')

print(f'You have {lettuce} lettuce.')
# You have 1 lettuce.

# ---------------------------------------------------------------------------------------- #
# using .append() method
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.append('Lettuce')
print(veggies)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce', 'Lettuce']

lettuce = veggies.count('Lettuce')
print(f'You have {lettuce} lettuce.')
# You have 2 lettuce.

# ---------------------------------------------------------------------------------------- #
# using .index() method
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
asparagus = veggies.index('Asparagus')

print(f'Asparagus is at index {asparagus}')
# Asparagus is at index 3

# .index() requires you to stay within range
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
asparagus = veggies.index('Asparagus', 4)

print(f'Asparagus is at index {asparagus}')
# Traceback (most recent call last):
#   File "C:/python/justhacking/lists.py", line 2, in <module>
#     asparagus = veggies.index('Asparagus', 4)
# ValueError: 'Asparagus' is not in list

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
celery = veggies.index('Celery', 1, 3)

print(f'Celery is at index {celery}')
# Celery is at index 2

# ---------------------------------------------------------------------------------------- #
# the enumerate() function is great
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
for i, veggie in enumerate(veggies):
    print(f'{veggie} is at index {i}')
# Kale us at index 0
# Cabbage us at index 1
# Celery us at index 2
# Asparagus us at index 3
# Lettuce us at index 4

# ---------------------------------------------------------------------------------------- #
# accees items with square brackets
print(veggies[1])
print(veggies[0])
print(veggies[3])
print(veggies[2])
print(veggies[4])
# Cabbage
# Kale
# Asparagus
# Celery
# Lettuce

# ---------------------------------------------------------------------------------------- #
# reverse a list
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.reverse()

print(veggies)
# ['Lettuce', 'Asparagus', 'Celery', 'Cabbage', 'Kale']

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.reverse()

# veggies is now ['Lettuce', 'Asparagus', 'Celery', 'Cabbage', 'Kale']
asparagus = veggies.index('Asparagus')
print(f'Asparagus is at index {asparagus}')
# Asparagus is at index 1

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.reverse()

asparagus = veggies.index('Asparagus')
print(f'Asparagus is at index {asparagus}')

veggies.reverse()

asparagus = veggies.index('Asparagus')
print(f'Now it is at index {asparagus}')
# Asparagus is at index 1
# Now it is at index 3

# ---------------------------------------------------------------------------------------- #
# clear a list with .clear()
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.clear()

print(veggies)
# []

# ---------------------------------------------------------------------------------------- #
# copy a list using .copy()
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies_copy = veggies.copy()

print(veggies)
print(veggies_copy)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']

print(id(veggies))
print(id(veggies_copy))
# 58068200
# 58067816

# pseudo copy (copy via reference)
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies_copy = veggies

print(id(veggies))
print(id(veggies_copy))
# 59313384
# 59313384

# ---------------------------------------------------------------------------------------- #
# add lists with .extend()
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
moar_veggies = ['Okra', 'Garlic']

veggies.extend(moar_veggies)

print(veggies)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce', 'Okra', 'Garlic']

# works with tuples
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
moar_veggies = ('Okra', 'Garlic')

veggies.extend(moar_veggies)

print(veggies)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce', 'Okra', 'Garlic']

# works with dictionaries
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
moar_veggies = {'Okra', 'Garlic'}

veggies.extend(moar_veggies)

print(veggies)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce', 'Okra', 'Garlic']

# works with strings
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
moar_veggies = 'Broccoli'

veggies.extend(moar_veggies)

print(veggies)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce', 'B', 'r', 'o', 'c', 'c', 'o', 'l', 'i']

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
moar_veggies = {'Broccoli': 'Yummy'}

veggies.extend(moar_veggies)

print(veggies)
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce', 'Broccoli']

# insert into a list with .insert()
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.insert(0, 'Spinach')

print(veggies)
# ['Spinach', 'Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.insert(2, 'Tomato')

print(veggies)
# ['Kale', 'Cabbage', 'Tomato', 'Celery', 'Asparagus', 'Lettuce']

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggie_tuple = ('Turnip', 'Cucumber')
veggies.insert(2, veggie_tuple)

print(veggies)
# ['Kale', 'Cabbage', ('Turnip', 'Cucumber'), 'Celery', 'Asparagus', 'Lettuce']

# ---------------------------------------------------------------------------------------- #
# pop an item off of the end of the list with .pop()
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
most_favorite = veggies.pop()

print(most_favorite)
# Lettuce

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
least_favorite = veggies.pop(0)

print(least_favorite)
# Kale

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
least_favorite = veggies.pop(5)

print(least_favorite)
# Traceback (most recent call last):
#   File "C:/python/justhacking/lists.py", line 2, in <module>
#     least_favorite = veggies.pop(5)
# IndexError: pop index out of range

# ---------------------------------------------------------------------------------------- #
# use .remove() if you don't know the index position
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.remove('Kale')

print(veggies)
# ['Cabbage', 'Celery', 'Asparagus', 'Lettuce']

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.remove('Celery')

print(veggies)
# ['Kale', 'Cabbage', 'Asparagus', 'Lettuce']

# ---------------------------------------------------------------------------------------- #
# The sort() method modifies the original list in place.
veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.sort()

print(veggies)
# ['Asparagus', 'Cabbage', 'Celery', 'Kale', 'Lettuce']

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']
veggies.sort(reverse=True)

print(veggies)
# ['Lettuce', 'Kale', 'Celery', 'Cabbage', 'Asparagus']

# ---------------------------------------------------------------------------------------- #
# create a list with list()
veggies = ('Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce')

print(veggies)
# ('Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce')
print(list(veggies))
# ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']

# ---------------------------------------------------------------------------------------- #
# using random with a list
import random

veggies = ['Kale', 'Cabbage', 'Celery', 'Asparagus', 'Lettuce']

surprise = random.choice(veggies)
# Lettuce

print(surprise)
