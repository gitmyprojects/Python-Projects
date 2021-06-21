from abc import ABC
class Shape(ABC):
    def print(self):
        print("I am a normal method defined inside the abstract class 'Shape'")
    def calculate_area(self):
        pass

class Rectangle(Shape): # child class
    length = 5
    breadth = 3
    def calculate_area(self): #defining parent abstract method
        return self.length * self.breadth

rec = Rectangle() #object created for the class 'Rectangle'
rec.print()

print("Area of a rectangle: ", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'
