# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:50:28 2024
Creates a class named "Pet" and a program that uses this class 
to ask a user for their pet specifics 
"""

# Defines the class we'll be using for the main program

class Pet: 
    """class to define pets"""
    def __init__(self, name='', pet_type='', age=0):
        """Initalize the pet object with default values"""
        self.name = name # Name
        self.pet_type = pet_type # Type
        self.age = age # Age
        
    def getName(self):
        """Returns the name of the pet."""
        return self.name
   
    def getType(self):
        """Returns the type of the pet."""
        return self.pet_type
    
    def getAge(self):
        """Returns the age of the pet."""
        return self.age
    
    def __repr__(self):
        """Return basic pet info"""
        return(f'{name}, {pet_type}, {age}')
    
    def __str__(self):
        """Return a more user friendly version of pet info"""
        return(f"Your {pet_type}s name is {name}, and they're {age} years old! ")
    
# The main program that will be using the "Pet" class
name = input(str("Whats your pets name :D ?\n"))
pet_type = input(str("And what type of animal are they?\n"))
age = input(str("And finally, how old are they?\n"))

my_pet = Pet(name, pet_type, age)
print('\n',my_pet)

print("\nThe pet's name is", my_pet.getName())
print("The pet's age is", my_pet.getAge())
print("The pet's type is", my_pet.getType())



    