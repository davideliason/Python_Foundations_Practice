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

        