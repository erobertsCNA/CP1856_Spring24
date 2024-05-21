# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:28:43 2024

@author: Arun.Rameshbabu
"""

print("The Miles Per Gallon Program\n")
miles = int(input("Enter miles driven:\t\t\t"))
gallons_gas = int(input("Enter gallons of gas used:\t"))

if gallons_gas > 0:
    mpg = miles/gallons_gas
    print(f"Miles per gallon:\t\t\t{mpg:.1f}")
else:
    print("Gallons used must be greater than zero. Try again.")

print("\nBye!")
