# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:
from enum import Enum
from abc import ABC, abstractmethod


class Animal(ABC):
    
    def __init__(self) -> None:
        print(f'{type(self).__name__} constructed!')

    @abstractmethod
    def move(self, move = 'walking') -> None:
        print(f'{type(self).__name__} {move}...')
    
    @abstractmethod
    def eat(self) -> None:
        print(f'{type(self).__name__} eating...')


class Dog(Animal):
    def __init__(self) -> None:
        Animal.__init__(self)

    def move(self) -> None:
        Animal.move(self)
    
    def eat(self) -> None:
        Animal.eat(self)


class Fish(Animal):
    def __init__(self) -> None:
        Animal.__init__(self)

    def move(self) -> None:
        Animal.move(self, 'swimming')

    def eat(self) -> None:
        Animal.eat(self)


class Bird(Animal):
    def __init__(self) -> None:
        Animal.__init__(self)

    def move(self) -> None:
        Animal.move(self, 'flying')

    def eat(self) -> None:
        Animal.eat(self)


dog = Dog()
dog.move()
dog.eat()

fish = Fish()
fish.move()
fish.eat()

bird = Bird()
bird.move()
bird.eat()













































# Solution:
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#
#     def move(self):
#         print("Animal Moving...")
#
#     def eat(self):
#         print("Animal Eating...")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Bird flying...")
#
#
#
# class Fish(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Fish Swimming...")
#
#
# class Dog(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Dog Running ...")
#
# mydog = Dog(3, "wolfy")
# mydog.move()
# mydog.eat()
#
# mydog = Fish(1, "nemo")
# mydog.move()
# mydog.eat()
#
# mydog = Bird(3, "jojo")
# mydog.move()
# mydog.eat()