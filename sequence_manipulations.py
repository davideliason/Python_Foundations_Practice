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




