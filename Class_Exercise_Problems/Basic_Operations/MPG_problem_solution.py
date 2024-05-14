# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:40:47 2024

@author: Arun.Rameshbabu
"""

print("The Miles Per Gallon program \n") # \n stands for newline
miles_driven = float(input("Enter miles driven:\t\t\t\t")) #\t stands for tab-space
gas_used = float(input("Enter gallons of gas used:\t\t")) #\t stands for tab-space
print()

# Doing the math
miles_per_gallon = miles_driven / gas_used
print(f"Miles per gallon:\t\t\t\t{miles_per_gallon:.2f}\n")
print("Bye!")
