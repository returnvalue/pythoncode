# Using composition to build complex objects
class Tractor():
    def __init__(self, model, make, engine=None):
        self.model = model
        self.make = make

        # Use references to other objects, like Engine and Implement
        self.engine = engine
        self.implements = []

    def addimplement(self, implement):
        self.implements.append(implement)

    def get_tractor_implements(self):
        return self.implements


class Engine():
    def __init__(self, cylinders, horsepower):
        self.cylinders = cylinders
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.cylinders} cylinder {self.horsepower} horsepower"


class Implement():
    def __init__(self, attachment_type):
        self.attachment_type = attachment_type


engine1 = Engine(3, 25)
tractor1 = Tractor("John Deere", "1025R", engine1)

tractor1.addimplement(Implement("Loader"))
tractor1.addimplement(Implement("Backhoe"))
tractor1.addimplement(Implement("Mowing Deck"))
tractor1.addimplement(Implement("Snowblower"))

print(f"This is a {tractor1.model} tractor.")
print(f"It has {tractor1.engine} engine.")
attachments = tractor1.get_tractor_implements()
print("The attachments it has include: ")
for attachment in attachments:
    print(" - " + attachment.attachment_type)