# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:46:57 2024

@author: Evan Roberts
"""

"""
Algorithm for how to achieve the solution - baseball program part 2

print decorator
print title
print menu
print decorator

while True:
menu_option <- input
if menu_option == '1':
    print statement
    at_bats <- int(input)
    hits <- int(input)
    batting_ave = hits/at_bats
    print batting_ave statement. 
elif menu_option == '2':
    print Bye!
else:
    print statement "Not a valid option. Please try again."

choice = '1'
while choice.lower() == '1':
    choice = menu_option = int(input("Menu option:\t"))
"""

print('='*40)
print("\t\t\tBaseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit program")
print('='*40)


while True:
    menu_option = input("Menu option:\t")
    if menu_option == '1':
        print("Calculate batting average...")
        number_bats = int(input("Official nnumber of at bats:\t"))
        number_hits = int(input("Number of hits:\t"))
        batting_ave = number_hits/number_bats
        print(f"Batting average:\t{batting_ave:.3f}\n")
    elif menu_option == '2':
        print("Bye!")
        break
    else:
        print("Not a valid option. Please try again")
        
        """
    elif menu_option == 2:
        print("Bye!")
        break
    else:
        print("Not a valid option. Please try again")
        
        """
    
    
    print("Bye!")
    break