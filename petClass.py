"""
You must use Classes and Objects to implement this project. The objective of 
Project 3 is to create a Pet class, read data from a text file, create objects 
and populate the data attributes and output the fields using the class’s 
mutator, accessor and __str__( ) methods.

Create a class named Pet, which should have the following private data 
attributes:
• __petName (the name of the pet as a single string)
• __petSpecies (commonly known species name)
• __petFamilyType (the family type of animal that the pet is. Example
values are ‘dog’, ‘cat’, ‘bird’, ‘snake, ‘fish’ and ‘insect’)
• __petOwnerName (owner’s name as a single string)

The Pet class should have an __init__( ) method that initializes these 
attributes.
This __init__ method can assign the values directly or call mutator methods to 
assign the values.

The Pet class should also have the following methods:
Mutator methods:
• set_Name – assigns a value to the __petName field
• set_Species – assigns a value to the __petSpecies field
• set_Family_Type – assigns a value to the __petFamilyType field
• set_Owner – assigns a value to the __petOwnerName field

Accessor methods:
• get_Name – returns the value of __petName field
• get_Species – returns the value of __petSpecies field
• get_Family_Type – returns the value of the __petFamilyType field
• get_owner – returns the value of the __petOwnerName field

Also create a __str__( ) method to call the accessor methods and output the 
data fields in the object.

Please store the class definition in a different file from the application 
program.
"""


# create the Pet class
class Pet:
    """
    The Pet class represents a pet with attributes such as name, species, 
    family type, and owner's name. It includes methods to modify and access 
    these attributes, as well as a method to return a string representation 
    of the pet's details.
    """
    
    # create the constructor for the Pet class
    # petName, petSpecies, petFamilyType, and petOwnerName are all private
    def __init__(self, name, species, familyType, ownerName):
        self.__petName = name
        
        self.__petSpecies = species
        
        self.__petFamilyType = familyType
        
        self.__petOwnerName = ownerName
        
    # create mutator methods (setters)
    # setName
    def setName(self, name):
        self.__petName = name
    
    # setSpecies
    def setSpecies(self, species):
        self.__petSpecies = species
    
    # setFamilyType
    def setFamilyType(self, familyType):
        self.__petFamilyType = familyType
    
    # setOwner
    def setOwner(self, ownerName):
        self.__petOwnerName = ownerName
    
    # create accessor methods (getters)
    # getName
    def getName(self):
        return self.__petName
    
    # getSpecies
    def getSpecies(self):
        return self.__petSpecies
    
    # getFamilyType
    def getFamilyType(self):
        return self.__petFamilyType
    
    # getOwner
    def getOwner(self):
        return self.__petOwnerName
        
    # str method
    def __str__(self):
        return (f"Pet Name: {self.__petName}, Pet Species: {self.__petSpecies}, Pet Family Type: {self.__petFamilyType}, Pet Owner Name: {self.__petOwnerName}")