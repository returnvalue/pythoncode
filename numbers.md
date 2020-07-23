In Python Number data types store numeric values. They are immutable data types, which means  
that changing the value of a number data type results in a newly allocated object.  

Python uses the + operator to add numbers.  
![](https://vegibit.com/wp-content/uploads/2020/06/Add-Integers-In-Python.png)

Adding floats works in a similar way.  
![](https://vegibit.com/wp-content/uploads/2020/06/How-To-Add-Floating-Point-Numbers-In-Python.png)

Subtraction is done with the – operator.  
![](https://vegibit.com/wp-content/uploads/2020/06/Python-Subtract-Numbers.png)

Division is done using the / operator. Notice they you don’t want to divide by zero, lest you run into a ZeroDivisionError.  
![](https://vegibit.com/wp-content/uploads/2020/06/How-To-Divide-Numbers-In-Python.png)

Here are a few examples of standard division vs integer floored quotient division.  
![](https://vegibit.com/wp-content/uploads/2020/06/Python-Integer-Floored-Quotient-Division.png)

The * operator handles multiplication for you.  
![](https://vegibit.com/wp-content/uploads/2020/06/Multiply-Python-Numbers.png)

The ** operator in Python allows you to calculate exponents like so.  
![](https://vegibit.com/wp-content/uploads/2020/06/How-To-Apply-An-Exponent-In-Python.png)

Find The Remainder  
![](https://vegibit.com/wp-content/uploads/2020/06/python-modulus-operator-example.png)

You can use parentheses just like algebra class to override the standard precedence if needed.  
![](https://vegibit.com/wp-content/uploads/2020/06/Python-math-order-of-operations-precedence.png)

To round a number in Python you can use the inbuilt round() function.  
![](https://vegibit.com/wp-content/uploads/2020/06/how-to-round-python-numbers.png)

round to 2 decimal places  
![](https://vegibit.com/wp-content/uploads/2020/06/python-round-2-decimal-places.png)

format float as percentage  
![](https://vegibit.com/wp-content/uploads/2020/06/python-format-float-as-percentage.png)

left padding with zeros  
![](https://vegibit.com/wp-content/uploads/2020/06/python-left-padding-with-zeros.png)

right padding with zeros  
![](https://vegibit.com/wp-content/uploads/2020/06/python-right-padding-with-zeros.png)

adding commas to large numbers  
![](https://vegibit.com/wp-content/uploads/2020/06/python-adding-commas-to-large-numbers.png)

* * *
Python Math Operators From Highest To Lowest Precedence

| Operator  |  Operation |  
|:----------|:-------------:|
| **        |  Exponent |  
| **%**     |  Modulus |  
| **//**    |  Integer Division |  
| **/**     |  Standard Division |  
| *****     |  Multiplication |  
| **–**     |  Subtraction |  
| **+**     |  Addition | 
* * *

```python
nums = [1, 3, 2, 5, 4]
sorted(nums)
```
[1, 2, 3, 4, 5]

```python
nums = [1, 3, 2, 5, 4]
sorted(nums, reverse=True)
```
[5, 4, 3, 2, 1]

```python
nums = {'a': 1, 'b': 3, 'c': 2, 'd': 5, 'e': 4}
sorted(nums.items(), key= lambda x: x[1])
```
[('a', 1), ('c', 2), ('b', 3), ('e', 4), ('d', 5)]

```python
nums = {'a': 1, 'b': 3, 'c': 2, 'd': 5, 'e': 4}
sorted(nums.items(), key= lambda x: x[1], reverse=True)
```
[('d', 5), ('e', 4), ('b', 3), ('c', 2), ('a', 1)]

These are the components of using sorted() with a dictionary.

| Parameter |  Syntax |  Meaning |  
|:-----:|:---------------:|:---------------|
| **object** |  nums.items() |  Refers to all values in our "nums" dictionary. If we were to use just "nums", we would have to reference the index position of the item to get its individual value. On the other hand, if we use nums.items(), an iterable list with the items in a list is created. |  
| **key** |  key=lambda x: x[1] |  A sorting mechanism that allows you to sort a dictionary by value. This is an example of a Lambda function, which is a function without a name. |  
| **reverse** |  reverse=True |  States that we want the numbers to be sorted in reverse, or descending order. | 
* * *

Printing numbers
```python
for num in range(1, 11):
    print(num)
```
1
2
3
4
5
6
7
8
9
10

```python
for num in range(0, 101, 10):
    print(num)
```
0
10
20
30
40
50
60
70
80
90
100

```python
for num in range(10, 0, -1):
    print(num)
```
10
9
8
7
6
5
4
3
2
1

```python
num = 916571163
[int(d) for d in str(num)]
```
[9, 1, 6, 5, 7, 1, 1, 6, 3]

```python
import string
 
for x, y in zip(range(1, 27), string.ascii_uppercase):
    print(x, y)
```
1 A
2 B
3 C
4 D
5 E
6 F
7 G
8 H
9 I
10 J
11 K
12 L
13 M
14 N
15 O
16 P
17 Q
18 R
19 S
20 T
21 U
22 V
23 W
24 X
25 Y
26 Z

```python
num = 123
print(bin(num))
```
0b1111011

```python
num = 123
print(f'{num:b}')
```
1111011