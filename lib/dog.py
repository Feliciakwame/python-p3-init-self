#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt"):
        self.breed = breed
        self.name = name
my_dog=Dog("Buddy")
print(my_dog.breed)
