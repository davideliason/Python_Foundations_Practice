#!/usr/bin/env python3
import helper_file_basics

with open("frankenstein.txt") as file:
	for line in file:
		print(helper_file_basics.upper_line(line))
		print("--------")
		print(helper_file_basics.lower_line(line))
		print("####")