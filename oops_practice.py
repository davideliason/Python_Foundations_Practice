"""
Examples with creating a classs, instantiating an object, and adding methods
"""
class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido=Dog()
fido.years=3
print(fido.dog_years())

# another example

class Book:
    name = "Dune"
    years = 0
    def speak(self):
        print("Read me, I am {}".format(self.name))
    def book_age(self):
        return self.years * 10

"""
Constructor: here we create a class Person, and create a Constructor method and a method
"""

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("tom")
# Call the greeting method
print(some_person.greeting())

"""
Output: some_person = Person("Tom")
 		print(some_person.greeting())
 		output string : hi my name is Tom
"""

