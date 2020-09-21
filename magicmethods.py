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

    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare book to non-book type')

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare book to non-book type')

        return self.price >= value.price

    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare book to non-book type')

        return self.price < value.price

    def __getattribute__(self, name):
        if (name == 'price'):
            price = super().__getattribute__('price')
            discount = super().__getattribute__('_discount')
            return price - (price * discount)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if (name == 'price'):
            if type(value) is not float:
                raise ValueError('The "price" attribute must be a float')
        return super().__setattr__(name, value)

    def __getattr__(self, name):
        return name + ' is not here!'

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


book1 = Book('Python Crash Course', 'Eric Matthes', 23.99)
book2 = Book('Serious Python', 'Julien Danjou', 25.43)
book3 = Book('Automate the Boring Stuff with Python', 'Al Sweigart ', 26.99)
book4 = Book('Python for Kids', 'Jason Briggs', 19.79)

# print each object
print(book1)
print(book2)
print(book3)
print(book4)

# use str() and repr()
print(str(book1))
print(repr(book2))

# Check for equality
print(book1 == book3)
print(book1 == book2)
print(book3 == book3)

# Check for greater and lesser value
print(book2 >= book1)
print(book2 < book1)
print(book3 >= book2)

# Sorting books
books = [book1, book3, book2, book4]
books.sort()
print([book.title for book in books])

# Try setting and accessing the price
book1.price = 37.95
print(book1)

book2.price = float(40)  # using an int will raise an exception
print(book2)

# If an attribute doesn't exist, __getattr__ will be called
print(book1.randomprop)

# call the object as if it were a function
print(book1)
book1('Learning Python', 'Mark Lutz', 44.94)
print(book1)
