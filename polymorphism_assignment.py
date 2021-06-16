# Parent
class Person:
    def __init__(self, name):
        self.name = name
   
    # To get name
    def getName(self):
        return self.name
   
    # To check if this person is an employee
    def isEmployee(self):
        return False

        # To check if this person is exempt
    def isExempt(self):
        return False
   

# Inherited
class Employee(Person):
    # return True to override the parent class
    def isEmployee(self):
        return True

class Exempt(Person):
    # return True to override the parent class
    def isExempt(self):
        return True


emp = Person("Cog")  # An Object of Person
print(emp.getName(), emp.isEmployee()) # methods in Parent class
   
emp = Employee("Worker Bee") # An Object of Employee
print(emp.getName(), emp.isEmployee())# same methods as parent class but overwritten

emp = Employee("Bossman") # An Object of a person who is Exempt
print(emp.getName(), emp.isExempt())
