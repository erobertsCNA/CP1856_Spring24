# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:54:21 2024

@author: Arun.Rameshbabu
"""

"""
Functions

Syntax
def function_name([arguments]):
    statements
    [return result]

"""

def print_welcome(message):
    print(message)
    print("This class is cool\n")

# Calling the function
print_welcome("This message was passed dynamically")
print_welcome("More such examples")    

# More examples
def miles_per_gallon(miles_driven, gallons):
    """
    This function takes in miles driven and gallons of fuel used to retun mpg

    Parameters
    ----------
    miles_driven : int / float
        Number of miles driven.
    gallons : int / float
        Gallons of gas used.

    Returns
    -------
    mpg : float
        Miles per gallon (mpg).

    """
    mpg = miles_driven/gallons
    return mpg

example = miles_per_gallon(100, 10)

miles_per_gallon(500, 14)
miles_per_gallon(miles_driven=500, gallons=14)

var1=500
var2=14
miles_per_gallon(var1, var2)
miles_per_gallon(miles_driven=var1, gallons=var2)

"""
Write the function to calculate the sales tax for the province of NL
Given function arguments:  
    sales_total
    tax_rate
returns
    tax_amount
"""

"""
Write the function to calculate the perimeter [and the area] of a rectangle
Given:
    side_a
    side_b
returns
    perimeter
"""