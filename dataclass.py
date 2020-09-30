class Book():
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'

    def __repr__(self):
        return f'title={self.title},author={self.author},price={self.price}'


book1 = Book('Python Crash Course', 'Eric Matthes', 23.99)
book2 = Book('Serious Python', 'Julien Danjou', 25.43)

# print each object
print(book1)
print(book2)
# Python Crash Course by Eric Matthes, costs 23.99
# Serious Python by Julien Danjou, costs 25.43

# use str() and repr()
print(str(book1))
print(repr(book2))
# Python Crash Course by Eric Matthes, costs 23.99
# title=Serious Python,author=Julien Danjou,price=25.43


from dataclasses import dataclass


@dataclass
class Book():
    title: str
    author: str
    price: float

    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'

    def __repr__(self):
        return f'title={self.title},author={self.author},price={self.price}'


book1 = Book('Python Crash Course', 'Eric Matthes', 23.99)
book2 = Book('Serious Python', 'Julien Danjou', 25.43)

# print each object
print(book1)
print(book2)
# Python Crash Course by Eric Matthes, costs 23.99
# Serious Python by Julien Danjou, costs 25.43

# use str() and repr()
print(str(book1))
print(repr(book2))
# Python Crash Course by Eric Matthes, costs 23.99
# title=Serious Python,author=Julien Danjou,price=25.43


from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f'{self.title} by {self.author}, {self.pages} pages'


# create some Book objects
book1 = Book('Python Crash Course', 'Eric Matthes', 544, 23.99)
book2 = Book('Serious Python', 'Julien Danjou', 225, 25.43)

# use the description attribute
print(book1.description)
print(book2.description)
# Python Crash Course by Eric Matthes, 544 pages
# Serious Python by Julien Danjou, 225 pages


from dataclasses import dataclass, field


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = 'Empty Book'
    author: str = 'Your Imagination'
    pages: int = 0
    price: float = 0.0


# Create a default book object
book1 = Book()
print(book1)

# Create a specified book, price is set by field operator
book1 = Book('Python Crash Course', 'Eric Matthes', 544, 23.99)
book2 = Book('Serious Python', 'Julien Danjou', 225, 25.43)
print(book1)
print(book2)
# Book(title='Empty Book', author='Your Imagination', pages=0, price=0.0)
# Book(title='Python Crash Course', author='Eric Matthes', pages=544, price=23.99)
# Book(title='Serious Python', author='Julien Danjou', pages=225, price=25.43)


from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    pages: int
    price: float

    # You can define methods in a dataclass like any other
    def bookinfo(self):
        return f'{self.title}, by {self.author}'


# create some instances
book1 = Book('Python Crash Course', 'Eric Matthes', 544, 23.99)
book2 = Book('Serious Python', 'Julien Danjou', 225, 25.43)

# access fields
print(book1.title)
print(book2.author)

# print the book itself - dataclasses provide a default
# implementation of the __repr__ function
print(book1)

# comparing two dataclasses
book3 = Book('Automate the Boring Stuff with Python', 'Al Sweigart ', 592, 26.99)
print(book1 == book3)

# change some fields, call a regular class method
book1.title = 'Python for Kids'
book1.pages = 864
print(book1.bookinfo())
# Python Crash Course
# Julien Danjou
# Book(title='Python Crash Course', author='Eric Matthes', pages=544, price=23.99)
# False
# Traceback (most recent call last):
#   File "C:/python/OOP/dataclass.py", line 33, in
#     book1.title = 'Python for Kids'
#   File "", line 3, in __setattr__
# dataclasses.FrozenInstanceError: cannot assign to field 'title'