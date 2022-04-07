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

"""
Special methods: summary:

Instead of creating classes with empty or default values, we can set these 
values when we create the instance. This ensures that we don't miss an important 
value and avoids a lot of unnecessary lines of code. To do this, we use a special
 method called a constructor. Below is an example of an Apple class with a constructor 
 method defined.

1234
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
When you call the name of a class, the constructor of that class is called. 
This constructor method is always named __init__. You might remember that special 
methods start and end with two underscore characters. In our example above, 
the constructor method takes the self variable, which represents the instance, 
as well as color and flavor parameters. These parameters are then used by the 
constructor method to set the values for the current instance. So we can now 
create a new instance of the Apple class and set the color and flavor values
 all in go:

123
>>> jonagold = Apple("red", "sweet")
>>> print(jonagold.color)
Red
In addition to the __init__ constructor special method, there is 
also the __str__ special method. This method allows us to define how an 
instance of an object will be printed when it’s passed to the print() function. 
If an object doesn’t have this special method defined, it will wind up using the 
efault representation, which will print the position of the object in memory. 
Not super useful. Here is our Apple class, with the __str__ method added:

1234567
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
...
Now, when we pass an Apple object to the print function, 
we get a nice formatted string:

123
>>> jonagold = Apple("red", "sweet")
>>> print(jonagold)
This apple is red and its flavor is sweet
This apple is red and its flavor is sweet

It's good practice to think about how your class might be used and to 
define a __str__ method when creating objects that you may want to print later.
