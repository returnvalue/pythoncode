# Multiple Inheritance Example
class One():
    def __init__(self):
        super().__init__()
        self.color = 'One color'
        self.name = 'Set In Class One'

    def karate_chop(self):
        print('Whack!')


class Two():
    def __init__(self):
        super().__init__()
        self.sound = 'Two sound'
        self.name = 'Set In Class Two'

    def karate_chop(self):
        print('Super Whack!!')


class Three(Two, One):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.color)
        print(self.sound)
        print(self.name)


# Instantiating An Object
obj_three = Three()

# MRO
print(Three.__mro__)

obj_three.showprops()

obj_three.karate_chop()


# Order Of Classes
class Three(One, Two):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.color)
        print(self.sound)
        print(self.name)


print(Three.__mro__)

obj_three.karate_chop()
