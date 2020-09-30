# Python allows you to read, write and delete files.
# Use the function open("filename","w+") to create a file. ...
# To append data to an existing file use the command open("Filename", "a")
# Use the read function to read the ENTIRE contents of a file.
# Use the readlines function to read the content of the file one by one.

# Reading an entire file at once
filename = 'pythonfile.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)
# This is a file.
#
# We can read it with Python.

# Showing the attributes and properties of the file
filename = 'pythonfile.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print('The filename is: ' + file_object.name)
print('The mode is: ' + file_object.mode)
# The filename is: pythonfile.txt
# The mode is: r

# Reading a file line by line
filename = 'pythonfile.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
# This is a file.
#
#
#
# We can read it with Python.

# use the rstrip() method which removes extra blank lines when printing to the screen.
filename = 'pythonfile.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
# This is a file.
#
# We can read it with Python.

# Modifying output during iteration
file_object = open('replace.txt', 'r')
print('File Contents\n' + file_object.read())
file_object.seek(0)

print('\nRevised Output')
for line in file_object:
    revised = line.replace('Spanish', 'Mexican')
    print(revised.rstrip())
file_object.close()
# File Contents
# Italian
# Chinese
# Spanish
#
# Revised Output
# Italian
# Chinese
# Mexican

# Storing the lines in a list
filename = 'pythonfile.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
print(lines)
# ['This is a file.\n', '\n', 'We can read it with Python.']

# Creating and writing to a file
filename = 'anotherfile.txt'
with open(filename, 'w') as file_object:
    file_object.write('Writing data to a file!')

# Write multiple lines to a file
filename = 'anotherfile.txt'
with open(filename, 'w') as file_object:
    file_object.write('This is line one!\n')
    file_object.write('This is line two.\n')

# Appending to a file
filename = 'anotherfile.txt'
with open(filename, 'a') as file_object:
    file_object.write('Appending this line to the file.\n')
    file_object.write('Appending another line to the file.\n')

# Open a file from a subfolder
file_path = 'subfolder/valuabledata.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# Using json.dump() to store data
import json
numbers = [3, 6, 9, 12, 15, 18]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

# Using json.load() to read data
filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
print(numbers)

# Using FileNotFoundError to manage data
file_name = 'nonexistent.json'
try:
    with open(file_name) as file_object:
        numbers = json.load(file_object)
except FileNotFoundError:
    message = f'Unable to find file: {file_name}.'
    print(message)
else:
    print(numbers)
# Unable to find file: nonexistent.json.

# Open a file for writing and create it if it doesn’t exist
file_object = open('pythonfile.txt', 'w+')

# Open the file for appending text to the end
file_object = open('pythonfile.txt', 'a+')

# Write some lines of data to the file
for i in range(10):
    file_object.write('This is line %d\r\n' % (i + 1))

# Close the file when done
file_object.close()

# Open the file back up and read the contents
file_object = open('pythonfile.txt', 'r')

# Check to make sure that the file was opened
# use the read() function to read the entire file
if file_object.mode == 'r':
    contents = file_object.read()
    print (contents)

# readlines() reads the individual lines into a list
if file_object.mode == 'r':
    file_lines = file_object.readlines()
    for line in file_lines:
        print(line)

# Using Temporary Files With Python
import tempfile

# Create a temporary file
temp_file = tempfile.TemporaryFile()

# Write to a temporary file
temp_file.write(b'Save the date: 070420')
temp_file.seek(0)

# Read the temporary file
print(temp_file.read())

# Close the temporary file
temp_file.close()

# Create a zip file
# Zipfile Module
import zipfile

# create a ZipFile object
zip_object = zipfile.ZipFile('FileArchive.zip', 'w')

# Add two files to the zip_object
zip_object.write('ships.txt')
zip_object.write('characters.txt')

# close the Zip File
zip_object.close()

# Open and List contents
zip_object = zipfile.ZipFile('FileArchive.zip', 'r')
print(zip_object.namelist())

# Metadata in the zip archive
for meta in zip_object.infolist():
    print(meta)

# Read a file in the zip archive
print(zip_object.read('ships.txt').decode("utf-8"))
# X-Wing
# Millennium Falcon
# Y-wing
# B-wing
# The Ghost
# Jedi Starfighter
# The Fireball

with zip_object.open('characters.txt') as file_object:
    print(file_object.read().decode("utf-8"))
# Bowser
# Princess Peach
# Toad
# Luigi
# Wario
# Yoshi
# Rosalina

zip_object.extract('ships.txt')
zip_object.extract('characters.txt')
zip_object.extractall()
			
			
			
