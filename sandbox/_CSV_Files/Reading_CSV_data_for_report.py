#!/usr/bin/env python3

import csv

# read_employees will receive CSV file as a parameter
# return a list of dictionaries from that file

# FUNCTION #1: READ EMPLOYEES



"""
DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys. So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.

We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.

Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. We will now register a dialect empDialect.
"""


import os
import csv

# FUNCTION ONE: IMPORT EMPLOYEES DATA

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect') 

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list

