class Swimmer:
    def move(self):
        print("Swimming in the water!")

class Flyer:
    def move(self):
        print("Flying in the sky!")

class Duck(Swimmer, Flyer):
    def move(self):
        print("Duck is moving!")
        super().move()

duck = Duck()
duck.move()

print(f"MRO order:",Duck.__mro__)