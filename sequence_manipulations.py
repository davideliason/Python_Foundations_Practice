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

  