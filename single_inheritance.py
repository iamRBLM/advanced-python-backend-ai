class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic animal sound!")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        super().make_sound()
        print("woof wooff!")

dog = Dog("Bingo", 20)
dog.make_sound()