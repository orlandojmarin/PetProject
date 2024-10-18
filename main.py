"""
Name: Orlando Marin
Class: Data Structures - CSC 212

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

To develop the application program, the attached text data file contains data 
you can use to create Pet objects. Each data line corresponds to data for a 
Pet object, given in the format: pet name, pet species, pet family type, and 
owner’s name.  There are 9 lines of data for 9 pet objects.

As a first phase, develop the application program is to take the data from the 
text file and to create and output the content of the 9 pet objects. This 
ensures that the class definition and application are written correctly before 
you go to the next step.

As a second phase, redesign your application program to use a list of objects 
as your data structure. Instead of reading the text data into various pet 
objects, build them into a list of pet objects. You should be able to use the 
same Pet class definition. 

Demonstrate how you can achieve all the functionality 
using this new data structure. Output the content of the list of pets. 

In addition, find all owner(s) with snake family type and insect family type 
pets. Output their names and their respective pet's name.
You only need to show the second phase as your final submission.
"""
# import petclass file and pydoc
import petClass
import pydoc


def main():
    """
    The main function performs the following tasks:

    1. Opens and reads data from 'petdata.txt', where each line represents a 
    pet's information.
    2. Creates Pet objects using the data from each line, storing them in a 
    list (`petList`).
    3. Outputs the names of owners who have pets from the 'snake' and 'insect' 
    family types, along with the pets' names.
    4. Closes the input file after reading and processing all the data.

    Additionally, the program uses `pydoc` to generate documentation for the 
    `main` function.
    """
    
    # create an empty list of pet objects
    petList = []
    
    # open the file petdata.txt to read from
    infile = open("/Users/orlandomarin/Downloads/petdata.txt", "r")
    
    # iterate through each line of the file
    for line in infile:
        # remove the newline character from the end of each line in the text file
        fileLine = line.rstrip("\n")
        
        # split each line of the text file by the space
        petData = fileLine.split(" ")
        
        # assign pet name
        petName = petData[0]
        
        # assign pet species
        petSpecies = petData[1]
        
        # assign pet family type
        petFamilyType = petData[2]
        
        # assign pet owner's name
        petOwnerName = petData[3]
        
        # create a pet
        pet = petClass.Pet(petName, petSpecies, petFamilyType, petOwnerName)
        
        # add the pet to the list "petList"
        petList.append(pet)
        
    # close the file
    infile.close()
    
    # print the owners and pet names with pet snakes
    print("Here are the owners with pet snakes and the names of the snakes:")
    for pet in petList:
        if pet.getFamilyType() == "snake":
            print(f"Owner name: {pet.getOwner()}, Snake name: {pet.getName()}")
    
    # print the owners and pet names with pet insects
    print("\nHere are the owners with pet insects and the names of the insects:")   
    for pet in petList:          
        if pet.getFamilyType() == "insect": 
            print(f"Owner name: {pet.getOwner()}, Insect name: {pet.getName()}")


# call main
if __name__ == "__main__":
    main()

# documentation
pydoc.writedoc("main")
pydoc.writedoc("petClass")

