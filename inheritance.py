# A Python Class
class Superclass():
    def __init__(self, color, height, width):
        self.height = height
        self.color = color
        self.width = width

    def does_stuff(self):
        print('This method does stuff')


# Inheriting From A Superclass
class Subclass(Superclass):
    pass


obj1 = Subclass('Red', '5 feet', 100)

# The Child Has Now Inherited Attributes And Methods
print(type(obj1))
# <class '__main__.Subclass'>

print(isinstance(obj1, Subclass))
# True

print(obj1.color)
# Red

print(obj1.height)
# 5 feet

print(obj1.width)
# 100

obj1.does_stuff()


# This method does stuff


# Classes Without Inheritance
class Inputdevice:
    def __init__(self, devicetype, inputconnector, bluetooth, manufacturer):
        self.devicetype = devicetype
        self.manufacturer = manufacturer
        self.inputconnector = inputconnector
        self.bluetooth = bluetooth


class Outputdevice:
    def __init__(self, devicetype, connector, manufacturer, outrate):
        self.devicetype = devicetype
        self.manufacturer = manufacturer
        self.outrate = outrate
        self.connector = connector


class IODevice:
    def __init__(self, devicetype, connector, manufacturer, outrate):
        self.devicetype = devicetype
        self.manufacturer = manufacturer
        self.outrate = outrate
        self.connector = connector


input1 = Inputdevice("Keyboard", "usb", True, "Lenovo")
io1 = IODevice("Flash Drive", "usb", "Sandisk", "35MB ps")
output1 = Outputdevice("Monitor", "HDMI", "Samsung", "18Gbps")

print("This device has a " + input1.inputconnector + " connector")
# This device has a usb connector

print(io1.manufacturer + " is the device manufacturer")
# Sandisk is the device manufacturer

print(input1.manufacturer + " " + input1.devicetype)
# Lenovo Keyboard

print(output1.manufacturer + " " + output1.devicetype)
# Samsung Monitor


# Rewriting Classes With Inheritance
class Peripheral:
    def __init__(self, devicetype, manufacturer):
        self.devicetype = devicetype
        self.manufacturer = manufacturer


class Outputperipheral(Peripheral):
    def __init__(self, devicetype, manufacturer, connector, outrate):
        super().__init__(devicetype, manufacturer)
        self.outrate = outrate
        self.connector = connector


class Inputdevice(Peripheral):
    def __init__(self, devicetype, inputconnector, bluetooth, manufacturer):
        super().__init__(devicetype, manufacturer)
        self.inputconnector = inputconnector
        self.bluetooth = bluetooth


class Outputdevice(Outputperipheral):
    def __init__(self, devicetype, connector, manufacturer, outrate):
        super().__init__(devicetype, manufacturer, connector, outrate)


class IODevice(Outputperipheral):
    def __init__(self, devicetype, connector, manufacturer, outrate):
        super().__init__(devicetype, manufacturer, connector, outrate)


input1 = Inputdevice("Keyboard", "usb", True, "Lenovo")
io1 = IODevice("Flash Drive", "usb", "Sandisk", "35MB ps")
output1 = Outputdevice("Monitor", "HDMI", "Samsung", "18Gbps")

print("This device has a " + input1.inputconnector + " connector")
# This device has a usb connector

print(io1.manufacturer + " is the device manufacturer")
# Sandisk is the device manufacturer

print(input1.manufacturer + " " + input1.devicetype)
# Lenovo Keyboard

print(output1.manufacturer + " " + output1.devicetype)
# Samsung Monitor
