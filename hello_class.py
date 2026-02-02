class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Cat:
    def __init__(self,name, color):
        self.name = name
        self.color = color

jerry = Dog(name="Jerry", breed="Desi")
tim = Dog("Tim", "Desi")


print(jerry.name, jerry.breed)
print(tim.name, tim.breed)