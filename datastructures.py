# Data structures are basically just that - they are structures which can hold some
# data together. In other words, they are used to store a collection of related data.

# array
import array

one_dimensional = array.array('i', [3, 6, 9, 12, 15])
for i in range(0, len(one_dimensional)):
    print(one_dimensional[i])
# 3
# 6
# 9
# 12
# 15

# Accessing every other element of the array
one_dimensional = array.array('i', [3, 6, 9, 12, 15])
for i in range(0, len(one_dimensional), 2):
    print(one_dimensional[i])
# 3
# 9
# 15

# Accessing an element directly
one_dimensional = array.array('i', [3, 6, 9, 12, 15])

print(one_dimensional[4])
# 15

# Lists are more user friendly than true arrays
empty_list = []

list_of_ints = [3, 6, 9]

mixed_list = [2, 'Boo', 3.14]

two_dimensional_list = [[3, 6, 9], [2, 'Boo', 3.14]]


# Singly linked list data structure
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def delete(self, index):
        if index > self.count:
            return
        if self.head == None:
            return
        else:
            tempIndex = 0
            node = self.head
            while tempIndex < index - 1:
                node = node.get_next()
                tempIndex += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def print_list(self):
        tempnode = self.head
        while (tempnode != None):
            print('Node: ', tempnode.get_data())
            tempnode = tempnode.get_next()


linkedlist = LinkedList()
linkedlist.insert(3)
linkedlist.insert(6)
linkedlist.insert(9)
linkedlist.insert(12)
linkedlist.insert(15)
linkedlist.print_list()
# Node:  15
# Node:  12
# Node:  9
# Node:  6
# Node:  3

print('Number of items in List: ', linkedlist.get_count())
# 5

print('Finding item: ', linkedlist.find(6))
# Finding item:  <__main__.Node object at 0x03512FD0>
print('Finding item: ', linkedlist.find(9))
# Finding item:  <__main__.Node object at 0x03538028>

linkedlist.delete(3)
print('Number of items in List: ', linkedlist.get_count())
print('Finding item: ', linkedlist.find(12))
linkedlist.print_list()
# Number of items in List:  4
# Finding item:  <__main__.Node object at 0x031A8058>
# Node:  15
# Node:  12
# Node:  9
# Node:  3

# Stack Data Structure
stack = []

stack.append('Tom')
stack.append('Dick')
stack.append('Harry')
stack.append('Bosch')
print(stack)
# ['Tom', 'Dick', 'Harry', 'Bosch']

popped = stack.pop()
print(popped)
print(stack)
# Bosch
# ['Tom', 'Dick', 'Harry']

# Stack as a Class
class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('Stack is empty')

    def size(self):
        return len(self.stack)


stack = Stack()
for i in range(5):
    stack.push(i)

print('Initial stack: ' + str(stack))
print('pop(): ' + str(stack.pop()))
print('After pop(), the stack is now: ' + str(stack))
stack.push(7)
print('After push(7), the stack is now: ' + str(stack))
print('The size is: ' + str(stack.size()))
# Initial stack: [0, 1, 2, 3, 4]
# pop(): 4
# After pop(), the stack is now: [0, 1, 2, 3]
# After push(7), the stack is now: [0, 1, 2, 3, 7]
# The size is: 5

# Queue data structure
from collections import deque

queue = deque()
queue.append('Monday')
queue.append('Tuesday')
queue.append('Wednesday')
queue.append('Thursday')
queue.append('Friday')
print(queue)
# deque(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

popped = queue.popleft()
print(popped)
print(queue)
# Monday
# deque(['Tuesday', 'Wednesday', 'Thursday', 'Friday'])

# Hash Table Data Structure
hashone = dict({'firstkey': 1, 'secondkey': 2, 'thirdkey': 'three'})
print(hashone)
# {'firstkey': 1, 'secondkey': 2, 'thirdkey': 'three'}

hashtwo = {}
hashtwo['firstkey'] = 1
hashtwo['secondkey'] = 2
hashtwo['thirdkey'] = 3
print(hashtwo)
# {'firstkey': 1, 'secondkey': 2, 'thirdkey': 3}

hashtwo['secondkey'] = 'two'
print(hashtwo)
# {'firstkey': 1, 'secondkey': 'two', 'thirdkey': 3}

for key, value in hashtwo.items():
    print('key: ', key, ' value: ', value)
# key:  firstkey  value:  1
# key:  secondkey  value:  two
# key:  thirdkey  value:  3
