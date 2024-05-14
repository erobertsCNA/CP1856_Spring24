# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:34:10 2024

@author: Arun.Rameshbabu
"""

print('='*64)
print('\t\t\t\t\tBaseball Team Manager\n')
print("This program calculates the batting average for a player based\non the player's official number of at bats and hits")
print('='*64)
print()
player_name = input("Player's name: ")
at_bats = int(input("Official number of at bats: "))
hits = int(input("Number of hits: "))

bat_average = hits / at_bats
print(f"\n{player_name}'s batting average is {bat_average:.3f}")
