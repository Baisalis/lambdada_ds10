"""
Define a class named rectangle which can be constructed by length and width

"""

class Rectangle:
    def __init__ (self , l , w):
        self.length = l
        self.width = w

    def area (self):
        """
        measure the are of the rectangle

        """
        return self.length * self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())
