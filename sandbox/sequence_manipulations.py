""" 
Objective; Given a list of filenames, rename all of the files with the extension hpp to the extension h.
"""

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

for x in filenames: # loop through input list, replace matching extension with desired extension, append new filename
    if x.endswith(".hpp"):  
        newfilename = x.replace(".hpp",".h")
        newfilenames.append(newfilename)
    else:           # if filename does not need to be changed, append directly to newfilename list
        newfilenames.append(x)
print(newfilenames) 
# Output as expected: ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

"""
Objective: create a function that turns text into pig lating by transforming each word thus: move the first 
           character of the word to the end of the word, and then add 'ay' to the very end
"""

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    # Select all characters from index position 1 until the end of string
    # Then add the first index character
    # Finally, add the ending to complete new string
    new_word = word[1:] + word[0]+"ay "
    # add this newly-modified word to the output say phrase
    say += new_word
    # Turn the list back into a phrase
  return say

  # Output as expected: 
  # print(pig_latin("hello how are you")) > ellohay owhay reaay auyay

"""
  Objective: create a function that takes an octet which expresses permission values,
             and return a string format instead (ex: permission octet of 7 is equal to "rwx")
             which is equal to "read, write, execute" permissions for a user. The input value 
             is numeric, which is converted within a list comprehension, first, into a string and then, second,
             into a list of octal digits (integers) which in turn is loops over (for loop) to compare 
             values and build the return string
"""

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += "-"
    return result

# Output as expected: print_octal_to_string(777) > "rwxrwxrwx"

"""
Objective: As input, accept a group name as string, and a list of string elements. Return a 
           string which combines the group name at the beginning, colon, then the string elements.
           To acheive this objective, I used the str.join() method, which combined the second argument
           string elements with a comma. This was combined with the group name for the final product.
"""

def group_list(group, users):
  members_to_string = ",".join(users)
  return "{}: {}".format(group, members_to_string)

# Input arguments: "Marketing", ["Mike","Joe"]
# Outut: "Marketing: Mike, Joe"

"""
Objective: Read in a list of tuples with three attributes: name, age, profession. 
           Loop through the list, and print out a custom string using those values
"""

def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as {}.".format(name,age,profession))

# Input guest_list([("John",30,"Pizza maker"),("Tim", 44, "Tech")])
# Output "John is 30 years old and works as a Pizza Maker"..


"""
Objective: Have a dictionary with multiple key values and multiple value values associated 
           with each key be looped through to combine each in unique output string
"""
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, properties in wardrobe.items():
    for x in properties:
        print("This {} has {} property".format(item,x))

# OUtput: "Red shirt", "blue shirt", ..."blue jeans", " black jeans"


"""
Objective: Have a parameter as single argument to a function, which includes domain names and associated 
           lists of user. Loop through each dictionary key-value pair, and combine
           each parent key with child values strings, to have as output valied email addresses
"""
def email_list(domains):
    emails = []
    for domain,users in domains.items():
      for user in users:
        emails.append("{}@{}".format(user,domain))
    return(emails)

# Output: email_lists({"gmail.com": ["joe.bob", "jill.her"], "yahoo.com": ["tim.bob", "sheryl.ladd"]})
#         Returns list as seen: ["joe.bob@gmail.com", etc]

"""
Objective: loop through dictionary and inner loop through key value pairs and create a new 
           dictionary that recomines values

def groups_per_user(group_dict):
    user_groups = {}
    for group, users in group_dict.items():
        # print(group) output: local, public, administrator
        for user in users:
            user_groups[user] = []
            user_groups[user].append(group)
    return user_groups

# Output: {"name_of_user": ["group1", "group2"]}

"""
Objective: Parse a given adrgument string and seperate the numeric part of address from 
           the text-only part of address name, then combine for output statement
"""
def format_address(address_string):
    house_number = ""
    streetname = ""
    
    split_address_string = address_string.split(" ")
    for part in split_address_string:
        if part.isdigit():
            house_number += part
        else:
            streetname += " " + part
    
    
    return "house # {} and street name {}".format(house_number, streetname)

# Output: format_address("123 Main St") > 123 on street named Main St

"""
Objective: count the frequency of letters in a given string. Do not count spaces, etc.append
"""

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower():
    # Check if the letter needs to be counted or not
    # convert any string characters to lowercase
    if letter.isalpha():
    # Add or increment the value in the dictionary
    # if the character is alphabetical, then count it
      if not letter in result:
        result[letter] = 1
      else:
        result[letter] += 1
  return result

"""
Output: invoking the function with string "AaBbCc" > {a:2, b:2, c:2}
"""
