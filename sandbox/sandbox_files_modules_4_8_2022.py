#!/usr/bin/env python3
import helper_file_basics

"""
with open("frankenstein.txt") as file:
# this will close the file auto after completed
	for line in file:
		print(helper_file_basics.upper_line(line))
		print("--------")
		print(line.strip().lower())

"""
file = open("frankenstein.txt","r")
lines = file.readlines()
file.close()

# now work with data in lines
# sort lines alphabetically

print(lines)

# read and write functions while adding and deleting elements
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))