# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:34:50 2024

@author: Arun.Rameshbabu
"""

# number = int(input("Enter an integer: "))
# print(f"The number entered is {number}")
# print("End of program")

"""
try:
    statements
except [ExceptionName]:
    statements
"""
try:
    number = int(input("Enter an integer: "))
    print(f"The number entered is {number}")
except Exception as e:
    print("You entered an invalid integer. Please try again.")
print("End of program")