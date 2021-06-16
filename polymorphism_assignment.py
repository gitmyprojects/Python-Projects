from math import pi


class Shape: # Parent Class
    def __init__(self, name):
        self.name = name

    def area(self):
        pass # the pass statement will define the function but not do anything. It's here so the child class can use(inherit) it

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self): #  string representation of an object. The object is 'name'.
        return self.name

# ------------------------------------------------------------------------------------------------

class Square(Shape): # Child of 'Shape' Parent
    def __init__(self, length):
        super().__init__("Square") # I initially used self but was getting a recursion error message.
        # I used w3 schools to learn about the super() method.
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."

    
# ------------------------------------------------------------------------------------------------

class Circle(Shape): # Child of 'Shape' Parent
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self): # I just happen to know about Pi in Math so I imported it. 
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
