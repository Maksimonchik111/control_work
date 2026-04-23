from abc import ABC, abstractmethod

# 1. Инкапсуляция

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age

        else:
            print("Ошибка, возраст не может быть отрицательным")


p = Person("oleg", 25)

print(p.get_age())

p.set_age(26)

print(p.get_age())




#2. Наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())
print(cat.name, cat.speak())


#3. Полиморфизм

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicyclе(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    print(vehicle.move())


car =Car()
bike = Bicyclе()
move(car)
move(bike)


#4. Абстракция

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


rect =Rectangle(10, 5)
circle = Circle(7)
print(rect.area())
print(circle.area())