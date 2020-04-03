# -*- coding: utf-8 -*-
"""04_tasks.py

Author -- Michael Widrich
Contact -- widrich@ml.jku.at
Date -- 01.10.2019

###############################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
manuscript, no matter whether as a whole or in parts, no matter whether in
printed or in electronic form, requires explicit prior acceptance of the
authors.

###############################################################################

Tasks for self-study. Try to solve these tasks on your own and
compare your solution to the solution given in the file 04_solutions.py.

"""

###############################################################################
# 04 Exceptions
###############################################################################

#
# Task 1
#

# Write a function that divides two numbers and returns the result. The
# numbers should be taken as keyword arguments with defaults of 1.0 for both
# values. If the division fails due to a ValueError or TypeError, print a
# warning and return None instead.

# Your code here

def my_division(first = 1.0, second = 1.0):
    try:
        div = first / second
        return div
    except (ValueError, TypeError) as er:
        print(f'warning: {er} try again')
        return None

print(my_division(5,3))
print(my_division(5, 'str'))

#
# Task 2
#

# Write a function add(value1, value2) that returns the sum of value1 and
# value2. If the addition fails due to a TypeError, convert the values
# to integers and return the sum of the two integers. If this fails due to
# a ValueError, convert the values to float and return the sum of the the
# two float values. If this fails due to a ValueError, raise the first
# exception from the first attempt at adding the values.

# Your code here #
def addy(value1, value2):
    try:
        adVal = value1 + value2
        return adVal
    except TypeError:
        value1 = int(value1)
        value2 = int(value2)
        adVal = value1 + value2
        return adVal
    except ValueError:
        value1 = float(value1)
        value2 - float(value2)
        
    
# Possible usage:
# print(add(5, 3))
# print(add(5, '3'))
# print(add(5, '3.'))
# print(add(5., '3'))
# print(add(5, '3.x'))
