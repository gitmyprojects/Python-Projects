
#parent class with two attributes
class animal:
    diet = 'primarily'
    form_of_movement = ' '

#child of 'animal' class   
class dogs(animal):
    #attributes in addition to parent class 'animal'
    breed = 'any'
    average_weight_lbs = 30

#child of 'animal' class
class snakes(animal):
    #attributes in addition to parent class 'animal' but not including
    #attributes of child class 'dogs'
    colors = 'orange and black'
    poisonous = True
    
