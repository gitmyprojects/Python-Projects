class Shape:
    __length = 0 #private variable
    __width = 0#private variable
    _height = 0#protected variable
    def __init__(self): #constructor
        self.__length = 5
        self.__width = 3
        self._height = 15
        #printing values of the private and protected variable within the class
        print(self.__length)
        print(self.__width)
        print(self._height)


shape = Shape() #object created that stores the class 'Shape'.

#printing values of the private/protected variables outside the class using the object created for the class 'Shape'
print(shape.length) # this attempts to call the method stored in the 'Shape' class and pass in 'length' but cant because length is protected. 
print(shape.width)
print(shape.height)

#the error is thrown because the varibles in the class 'Shape' are private/protected


