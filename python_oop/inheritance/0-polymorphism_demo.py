#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

animals = [Dog(), Cat(), Dog()]
for animal in animals:
    print(animal.speak())

print(isinstance(dog, Animal))
print(isinstance(cat, Dog))
print(isinstance(dog, Cat))
print(isinstance(cat, Animal))

print(issubclass(Dog, Animal))
