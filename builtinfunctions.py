# the len() function
meat = 'Bacon'
print('Bacon has ' + str(len(meat)) + ' characters')
# Bacon has 5 characters

veggie = 'Broccoli'
print('Broccoli has ' + str(len(veggie)) + ' characters')
# Broccoli has 8 characters

tickers = ['lk', 'msft', 'bynd', 'crc']
print('There are ' + str(len(tickers)) + ' tickers in the list')
# There are 4 tickers in the list

for i in range(0, len(tickers)):
    print(tickers[i])
# lk
# msft
# bynd
# crc

listofints = [1, 2, 3, 4, 5, 6, 7]
print(len(listofints))
# 7

tickerprices = {'lk': 45.50, 'msft': 165.70, 'crc': 8.25}
print('There are ' + str(len(tickerprices)) + ' tickers in the dictionary')
# There are 3 tickers in the dictionary

mixedtypes = [tickers, listofints, tickerprices, 'Superbowl', True]
print('There are ' + str(len(mixedtypes)) + ' items in the mixed list')
# There are 5 items in the mixed list

# range() and list()
team_members = range(25)
print(team_members)
print(len(team_members))
# 25

print(list(team_members))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

for player in list(team_members):
    print('Player ' + str(player))
# Player 0
# Player 1
# Player 2
# Player 3
# Player 4
# Player 5
# Player 6
# Player 7
# Player 8
# Player 9
# Player 10
# Player 11
# Player 12
# Player 13
# Player 14
# Player 15
# Player 16
# Player 17
# Player 18
# Player 19
# Player 20
# Player 21
# Player 22
# Player 23
# Player 24

team_a = []
team_b = []
for player in team_members:
    if player % 2 == 0:
        team_a.append(list(team_members).pop(player))
    else:
        team_b.append(list(team_members).pop(player))

for player in team_a:
    print('Player ' + str(player) + ' is on team A')

for player in team_b:
    print('Player ' + str(player) + ' is on team B')
# Player 0 is on team A
# Player 2 is on team A
# Player 4 is on team A
# Player 6 is on team A
# Player 8 is on team A
# Player 10 is on team A
# Player 12 is on team A
# Player 14 is on team A
# Player 16 is on team A
# Player 18 is on team A
# Player 20 is on team A
# Player 22 is on team A
# Player 24 is on team A
# Player 1 is on team B
# Player 3 is on team B
# Player 5 is on team B
# Player 7 is on team B
# Player 9 is on team B
# Player 11 is on team B
# Player 13 is on team B
# Player 15 is on team B
# Player 17 is on team B
# Player 19 is on team B
# Player 21 is on team B
# Player 23 is on team B

# min() and max()
print(max(-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5))
# 5
print(min(-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5))
# -5

jeans = 40
sweater = 50
shoes = 100
print(min(jeans, sweater, shoes))
# 40

print(max(jeans, sweater, shoes))
# 100

print(min('Kohls', 'Target'))
# Kohls

print(min('Bed Bath Beyond', 'Best Buy', 'Applebees'))
# Applebees

tshirt = 15
print(min(tshirt, sweater, jeans, shoes))
# 15

print(max(tshirt, sweater, jeans, shoes))
# 100

# round() abs() and pow()
frappuccino = 4.72
print(round(frappuccino))
# 5

blueberrypie = 3.14159265359
print(round(blueberrypie, 4))
# 3.1416

intnum = -7
print('Absolute value of -7 is:', abs(intnum))
# Absolute value of -7 is: 7

floatnum = -2.75
print('Absolute value of -2.75 is:', abs(floatnum))
# Absolute value of -2.75 is: 2.75

plantroot = -2.5
print(abs(plantroot))
# 2.5

print(pow(2, 10))
# 1024

# sorted()
randomnums = [12, -54, 32, 15, -7, 44]
sortednums = sorted(randomnums)
print(sortednums)
# [-54, -7, 12, 15, 32, 44]

reversednums = sorted(randomnums, reverse=True)
print(reversednums)
# [44, 32, 15, 12, -7, -54]

stores = ['Kohls', 'Target', 'Best Buy', 'Walmart', 'Costco']
print(sorted(stores))
# ['Best Buy', 'Costco', 'Kohls', 'Target', 'Walmart']

print(sorted(stores, reverse=True))
# ['Walmart', 'Target', 'Kohls', 'Costco', 'Best Buy']

stock_prices = {'Apple': 318.38, 'Google': 1487.64, 'Microsoft': 165.27, 'Cisco': 49.06}
for key in sorted(stock_prices.keys()):
    print(key, stock_prices[key])
# Apple 318.38
# Cisco 49.06
# Google 1487.64
# Microsoft 165.27

for key, value in sorted(stock_prices.items(), key=lambda item: item[1]):
    print(key, value)
# Cisco 49.06
# Microsoft 165.27
# Apple 318.38
# Google 1487.64

for key in sorted(stock_prices.keys(), reverse=True):
    print(key, stock_prices[key])
# Microsoft 165.27
# Google 1487.64
# Cisco 49.06
# Apple 318.38

for key, value in sorted(stock_prices.items(), key=lambda item: item[1], reverse=True):
    print(key, value)
# Google 1487.64
# Apple 318.38
# Microsoft 165.27
# Cisco 49.06

shirts = [('Blue', 'XL', 25), ('Red', 'L', 15), ('Green', 'S', 10), ('Yellow', 'M', 20)]

print(sorted(shirts, key=lambda item: item[0]))
# [('Blue', 'XL', 25), ('Green', 'S', 10), ('Red', 'L', 15), ('Yellow', 'M', 20)]

print(sorted(shirts, key=lambda item: item[1]))
# [('Red', 'L', 15), ('Yellow', 'M', 20), ('Green', 'S', 10), ('Blue', 'XL', 25)]

print(sorted(shirts, key=lambda item: item[2]))
# [('Green', 'S', 10), ('Red', 'L', 15), ('Yellow', 'M', 20), ('Blue', 'XL', 25)]


# type() and isinstance()
r = range(0, 20)
print(type(r))
# <class 'range'>

print(type(7))
# <class 'int'>

print(type('Z'))
# <class 'str'>

print(type('A simple string'))


# <class 'str'>

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color


class Truck(Car):
    def fourwheeldrive(self):
        print('four wheel drive engaged')


car = Car('Honda', 'Civic', 'Blue')
print(type(car))
# <class '__main__.Car'>

tesla = Car('Tesla', 'Model 3', 'White')
print(type(tesla))
# <class '__main__.Car'>

truck = Truck('Toyota', 'Tacoma', 'Red')
print(type(truck))
# <class '__main__.Truck'>

print(type(car) == type(truck))
# False
print(type(car) == type(tesla))
# True
print(isinstance(car, Car))
# True
print(isinstance(truck, Car))
# True
