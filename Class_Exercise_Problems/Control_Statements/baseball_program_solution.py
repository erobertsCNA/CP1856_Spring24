# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:37:00 2024

@author: Arun.Rameshbabu
"""

"""
Algorithm

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
        batting_avg = hits/at_bats
        print batting_avg statement\n
    elif menu_option == '2':
        print Bye!
        break
    else:
        print statement\n
"""
print('='*64)
print('\t\t\t\tBASEBALL TEAM MANAGER')
print('MENU OPTIONS')
print('1 - Calculate Batting Average')
print('2 - Exit program')
print('='*64)

while True:
    menu_option = input("Menu option: ")
    if menu_option == '1':
        print("Calculate batting average...")
        at_bats = int(input("Official number of at bats: "))
        hits = int(input('Number of hits: '))
        bat_avg = hits / at_bats
        print(f'Batting average: {bat_avg:.3f}\n')
    elif menu_option == '2':
        print('Bye!')
        break
    else:
        print('Not a valid option. Please try again.\n')
