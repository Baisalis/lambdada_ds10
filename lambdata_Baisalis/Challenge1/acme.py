import unittest
from random import randint

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

      

    def stealability(self):
        ratio = self.price / self.weight
        if ratio > 0.5:
            return "not so steable"
        elif ratio < 1.0:
            return "kinda steable"
        else: 
            return "very steable"


    def explode(self):
        ratio = self.flammability * self.weight
        if ratio < 10:
            return "fizzle."
        elif ratio < 50 :
            return "boom!"
        else:
            return "BABOOM!!"  

class BoxingGlove(Product):
    def __init__(self, name):
        super().__init__(name)
        self.weight = 10

    def explode(self):
        return "it is a glove."

    def punch(self):
        if  self.weight < 5 :
            return "that tickles."
        elif self.weight < 15 :
            return "hey that hurt!"
        else:
            return "ouch!"        




