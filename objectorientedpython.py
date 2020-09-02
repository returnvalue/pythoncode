# Basic Class Definition
class Monitor():
    def __init__(self, model):
        self.model = model


# Create Instances Of The Class
monitor1 = Monitor("Samsung")
monitor2 = Monitor("Viewsonic")

# Print The Class and Property
print(monitor1)
print(monitor1.model)
# <__main__.Monitor object at 0x01702E98>
# Samsung


print(monitor2)
print(monitor2.model)
# <__main__.Monitor object at 0x01042F28>
# Viewsonic
