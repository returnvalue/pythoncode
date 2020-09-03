class Monitor:
    def __init__(self, model, resolution, screensize, price):
        self.model = model
        self.resolution = resolution
        self.screensize = screensize
        self.price = price
        self.__revision = "A"

    def getPrice(self):
        if hasattr(self, "_discount"):
            return f"This monitor has a price of {self.price - self._discount:.2f}"
        else:
            return f"This monitor has a price of {self.price}"

    def setDiscount(self, amount):
        self._discount = amount


monitor1 = Monitor("Samsung", "1920 x 1080", "24 inch", 129.99)
monitor2 = Monitor("Viewsonic", "1920 x 1080", "24 inch", 109.99)
monitor3 = Monitor("Dell", "1920 x 1080", "27 inch", 159.99)

print(monitor2.getPrice())

monitor1 = Monitor("Samsung", "1920 x 1080", "24 inch", 129.99)
print(monitor1.getPrice())

monitor1.setDiscount(10)
print(monitor1.getPrice())

print(monitor1.__revision)

print(monitor1._Monitor__revision)
