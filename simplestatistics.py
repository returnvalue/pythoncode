import statistics
import math

grades = [80, 85, 77, 97, 100, 75, 88, 90, 93]

# Mean
# Here is how we calculate the mean(average) of all the grades in our list.

meangrades = statistics.mean(grades)
print(f'The mean of all the grades is {meangrades}')


# Median
# To calculate the Median, or midpoint of the grades, we’ll use this code here.
mediangrades = statistics.median(grades)
print(f'The median of all the grades is {mediangrades}')

# Sort to view the "middle"
print(sorted(grades))


# Now we can do the calculation of the mode like so.
grades = [75, 80, 85, 77, 97, 100, 75, 88, 75, 90, 93, 77]
modegrades = statistics.mode(grades)
print(f'The mode of all the grades is {modegrades}')


# Variance
grades = [75, 80, 85, 77, 97, 100, 75, 88, 75, 90, 93, 77]
variancegrades = statistics.variance(grades)

print(f'The grades have a variance of {variancegrades}')

grades = [90, 90, 90, 90, 90, 90]
variancegrades = statistics.variance(grades)

print(f'The grades have a variance of {variancegrades}')

grades = [90, 90, 90, 90, 90, 90, 100]
variancegrades = statistics.variance(grades)
print(f'The grades have a variance of {variancegrades}')

grades = [80, 82, 100, 77, 89, 94, 98, 50]
variancegrades = statistics.variance(grades)
print(f'The grades have a variance of {variancegrades}')


# Standard Deviation
grades = [89, 91, 95, 92, 93, 94, 98, 90]
stdevgrades = statistics.stdev(grades)

print(f'The grades have a standard deviation of {stdevgrades}')

grades = [30, 80, 100, 45, 15, 94, 64, 90]
stdevgrades = statistics.stdev(grades)

print(f'The grades have a standard deviation of {stdevgrades}')

grades = [30, 80, 100, 45, 15, 94, 64, 90]
stdevgrades = math.sqrt(statistics.variance(grades))

print(f'The grades have a standard deviation of {stdevgrades}')
