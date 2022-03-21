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