# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:00:04 2024

@author: Arun.Rameshbabu
"""

"""
While loop Syntax
while boolean_expression:
    statements...
"""

choice = "y"
while choice.lower() == 'y':
    print("Hey, this class is cool!")
    choice = input("Is the class still cool (y/n): ")
print("Bye!")

"""
Get a starting value from the user
Get a stop value from the user
Print the start vaue, increment and print the next value till you arrive at the stop value.
Here is an example:
Start Value: 4
Stop Value: 10

4 5 6 7 8 9 10
The loop has ended. Bye!
"""
start_value = int(input("Start Value: "))
stop_value = int(input("Stop Value: "))
print()
while stop_value >= start_value:
    print(start_value, end=" ")
    start_value += 1

print("\nThe loop has ended. Bye!")
