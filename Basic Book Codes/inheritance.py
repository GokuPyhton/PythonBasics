class Car:
    def __init__(self, name, mil):
        self.name = name
        self.mil = mil

    def description(self):
        return f"The name - {self.name} and mil of car is {self.mil}km/l"


class BMW(Car):
    pass


class Audi(Car):
    def display_audi(self):
        print("This is audi class")



b = BMW("BMW Car", 34.67)
print(b.description())

a = Audi("Audi Car", 54.45)
print(a.description())
a.display_audi()
