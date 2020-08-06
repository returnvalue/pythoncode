# Matplotlib is a plotting library for the Python programming language and its numerical
# mathematics extension NumPy. It provides an object-oriented API for embedding plots into
# applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.

import matplotlib.pyplot as plt

# plt.plot(x,y)
plt.plot([1, 2, 3], [2, 4, 3])

plt.show()

# Legends, Titles, and Labels
x = [1, 2, 3]
y = [2, 4, 3]

plt.plot(x, y)
plt.xlabel('X Label (Plot Number)')
plt.ylabel('Y Label (The Data)')

plt.title('My Cool Graph')
plt.show()

# Legend
x = [1, 2, 3]
y = [2, 4, 3]

x2 = [1, 2, 3]
y2 = [7, 7, 14]

plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
plt.xlabel('X Label (Plot Number)')
plt.ylabel('Y Label (The Data)')

plt.title('My Cool Graph')
plt.legend()
plt.show()

# bar()
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='First Bars')

plt.xlabel('X Label (Plot Number)')
plt.ylabel('Y Label (The Data)')

plt.title('My Cool Graph')
plt.legend()
plt.show()

# Side by side
x = [1, 3, 5, 7, 9]
y = [2, 4, 3, 1, 7]

x2 = [2, 4, 6, 8, 10]
y2 = [2, 4, 4, 2, 6]

plt.bar(x, y, label='First Bars')
plt.bar(x2, y2, label='Second Bars')

plt.xlabel('X Label (Plot Number)')
plt.ylabel('Y Label (The Data)')

plt.title('My Cool Graph')
plt.legend()
plt.show()

# Color of bars
plt.bar(x, y, label='First Bars', color='red')
plt.bar(x2, y2, label='Second Bars', color='black')

# Histogram
salaries = [55312, 88143, 57423, 65872, 68154, 77554, 72345, 79492, 52310, 88541, 97000, 105234, 73198]
bins = [50000, 60000, 70000, 80000, 90000, 100000]

plt.hist(salaries, bins, histtype='bar', rwidth=0.7)

plt.xlabel('Salaries')
plt.ylabel('Number of people')

plt.title('My Cool Histogram')

plt.show()

# Scatter Plots
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [9, 7, 3, 5, 2, 2, 1, 1, 6, 10]

plt.scatter(x, y)

plt.xlabel('This is X')
plt.ylabel('This is Y')

plt.title('My Cool Scatter Plot')

plt.show()

# Change marker
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [9, 7, 3, 5, 2, 2, 1, 1, 6, 10]

plt.scatter(x, y, marker='D', s=100)

plt.xlabel('This is X')
plt.ylabel('This is Y')

plt.title('My Cool Scatter Plot')

plt.show()

# Stack Plots
days = [1, 2, 3, 4, 5]

emails = [1, 1, 2, 3, 1]
codereviews = [2, 1, 1, 2, 3]
bugreports = [0, 0, 1, 0, 2]
internet = [3, 4, 2, 2, 5]

plt.stackplot(days, emails, codereviews, bugreports, internet,
              labels=['emails', 'codereviews', 'bugreports', 'internet'])

plt.xlabel('This is X')
plt.ylabel('This is Y')

plt.title('My Cool Stackplot')
plt.legend()
plt.show()

# Pie Charts
days = [1, 2, 3, 4, 5]

emails = [1, 1, 2, 3, 1]
codereviews = [2, 1, 1, 2, 3]
bugreports = [0, 0, 1, 0, 2]
internet = [3, 4, 2, 2, 5]

slices = [sum(emails), sum(codereviews), sum(bugreports), sum(internet)]
tasks = ['emails', 'codereviews', 'bugreports', 'internet']

plt.pie(slices, labels=tasks)

plt.title('My Cool Pie Chart')
plt.legend()
plt.show()

# Adjusting The Start Angle and Percentages
days = [1, 2, 3, 4, 5]

emails = [1, 1, 2, 3, 1]
codereviews = [2, 1, 1, 2, 3]
bugreports = [0, 0, 1, 0, 2]
internet = [3, 4, 2, 2, 5]

slices = [sum(emails), sum(codereviews), sum(bugreports), sum(internet)]
tasks = ['emails', 'codereviews', 'bugreports', 'internet']

plt.pie(slices, labels=tasks, startangle=90, autopct='%1.1f%%')

plt.title('My Cool Pie Chart')
plt.legend()
plt.show()

# Exploding a slice
days = [1, 2, 3, 4, 5]

emails = [1, 1, 2, 3, 1]
codereviews = [2, 1, 1, 2, 3]
bugreports = [0, 0, 1, 0, 2]
internet = [3, 4, 2, 2, 5]

slices = [sum(emails), sum(codereviews), sum(bugreports), sum(internet)]
tasks = ['emails', 'codereviews', 'bugreports', 'internet']

plt.pie(slices, labels=tasks, startangle=90,
        autopct='%1.1f%%', explode=(0, 0, 0.2, 0))

plt.title('My Cool Pie Chart')
plt.legend()
plt.show()

# Loading Data From Files
import csv

x = []
y = []

with open('fileondisk.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Data from fileondisk.txt')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Cool Chart')
plt.legend()
plt.show()

# Using Numpy
import numpy as np

x, y = np.loadtxt('fileondisk.txt', delimiter=',', unpack=True)
plt.plot(x, y, label='Data from fileondisk.txt')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Cool Chart')
plt.legend()
plt.show()

# Plotting Internet Data in matplotlib
import urllib
import matplotlib.dates as mdates


def dateconv(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def stock_data(stock):
    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + stock + '?period1=1553968903&period2=1585591303&interval=1d&events=history'
    result = urllib.request.urlopen(url).read().decode()
    graph_data = []
    split_result = result.split('\n')
    for line in split_result:
        split_line = line.split(',')
        if len(split_line) == 7:
            graph_data.append(line)
    graph_data.pop(0)
    date, open, high, low, close, adjclose, volume = np.loadtxt(graph_data, delimiter=',', unpack=True,
                                                                converters={0: dateconv('%Y-%m-%d')})
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('My Cool Chart')
    plt.plot_date(date, close)
    plt.legend()
    plt.show()


stock_data('MSFT')

# Matplotlib Styles
x = []
y = []

with open('fileondisk.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.style.use('seaborn-dark')
plt.plot(x, y, label='Data from fileondisk.txt')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('My Cool Chart')
plt.legend()
plt.show()

# Matplotlib XKCD Mode
x = []
y = []

with open('fileondisk.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

with plt.xkcd():
    plt.plot(x, y, label='Data from fileondisk.txt')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('My Cool Chart')
    plt.legend()
    plt.show()

# XKCD mode with a custom style
x = []
y = []

with open('fileondisk.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

with plt.xkcd():
    plt.style.use('dark_background')
    plt.plot(x, y, label='Data from fileondisk.txt')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('My Cool Chart')
    plt.legend()
    plt.show()