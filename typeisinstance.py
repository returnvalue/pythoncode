class Monitor():
    def __init__(self, model):
        self.model = model


class Keyboard():
    def __init__(self, model):
        self.model = model


monitor1 = Monitor("Panasonic")
monitor2 = Monitor("LG")
keyboard1 = Keyboard("Microsoft")
keyboard2 = Keyboard("IBM")

print(type(monitor1))
# <class '__main__.Monitor'>

print(type(keyboard1))
# <class '__main__.Keyboard'>

print(type(monitor1) == type(monitor2))
# True

print(type(monitor1) == type(keyboard2))
# False

print(isinstance(monitor1, Monitor))
# True

print(isinstance(keyboard1, Keyboard))
# True

print(isinstance(keyboard2, Monitor))
# False

print(isinstance(monitor1, object))
# True

print(isinstance(keyboard1, object))
# True

print(isinstance('Some String', object))
# True

print(isinstance(True, object))
# True

print(isinstance(7, object))
# True

print(isinstance(Monitor, object))
# True
print(isinstance(lambda x: x, object))
