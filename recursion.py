# Recursive Functions in Python: A recursive function is a function defined in terms of itself
# via self-referential expressions. This means that the function will continue to call
# itself and repeat its behavior until some condition is met to return a result.


# Recursion Example 1: Counting backward by 2
def backwardsby2(num):
    if num <= 0:
        print('Zero!')
        return
    else:
        emojismiles = []
        for i in range(0, num):
            emojismiles += '😃'
        print(num, ' '.join(emojismiles))
        backwardsby2(num - 2)


backwardsby2(9)
# 9 😃 😃 😃 😃 😃 😃 😃 😃 😃
# 7 😃 😃 😃 😃 😃 😃 😃
# 5 😃 😃 😃 😃 😃
# 3 😃 😃 😃
# 1 😃
# Zero!


# Recursion Example 2: Tower of Hanoi
def towerOfHanoi(numrings, from_pole, to_pole, aux_pole):
    if numrings == 1:
        print('Move ring 1 from', from_pole, 'pole to', to_pole, 'pole')
        return
    towerOfHanoi(numrings - 1, from_pole, aux_pole, to_pole)
    print('Move ring', numrings, 'from', from_pole, 'pole to', to_pole, 'pole')
    towerOfHanoi(numrings - 1, aux_pole, to_pole, from_pole)


numrings = 2
towerOfHanoi(numrings, 'Left', 'Right', 'Middle')
# Move ring 1 from Left pole to Middle pole
# Move ring 2 from Left pole to Right pole
# Move ring 1 from Middle pole to Right pole

# Calling function with 3 rings instead of 2
numrings = 3
towerOfHanoi(numrings, 'Left', 'Right', 'Middle')
# Move ring 1 from Left pole to Right pole
# Move ring 2 from Left pole to Middle pole
# Move ring 1 from Right pole to Middle pole
# Move ring 3 from Left pole to Right pole
# Move ring 1 from Middle pole to Left pole
# Move ring 2 from Middle pole to Right pole
# Move ring 1 from Left pole to Right pole


# Recursion Example 3: Set a number to a power
def power(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power(num, topwr - 1)


print('{} to the power of {} is {}'.format(4, 7, power(4, 7)))
print('{} to the power of {} is {}'.format(2, 8, power(2, 8)))
# 4 to the power of 7 is 16384
# 2 to the power of 8 is 256


# Recursion Example 4: Factorial function
def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num - 1)


print('{}! is {}'.format(4, factorial(4)))
print('{}! is {}'.format(2, factorial(2)))
# 4! is 24
# 2! is 2


# Recursion Example 5: Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 14

print('Fibonacci sequence:')
for i in range(number):
    print(fibonacci(i))
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233


# Recursion Example 6: Sum of numbers from 1 to n
def sumnums(n):
    if n == 1:
        return 1
    return n + sumnums(n - 1)


print(sumnums(3))
print(sumnums(6))
print(sumnums(9))
# 6
# 21
# 45


# Recursion Example 7: Reverse a string
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


reverseme = 'Desserts'
print(reverse(reverseme))
# stresseD

reverseme = 'Knits'
print(reverse(reverseme))
# stinK

reverseme = 'Regal'
print(reverse(reverseme))
# lageR

reverseme = 'Pupils'
print(reverse(reverseme))
# slipuP

reverseme = 'Smart'
print(reverse(reverseme))
# tramS

reverseme = 'Pals'
print(reverse(reverseme))
# slaP

reverseme = 'Straw'
print(reverse(reverseme))
# wartS

reverseme = 'Time'
print(reverse(reverseme))
# emiT

reverseme = 'Star'
print(reverse(reverseme))
# ratS