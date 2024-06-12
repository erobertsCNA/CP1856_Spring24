# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:57:10 2024

@author: Arun.Rameshbabu
"""

import random

"""
Algorithm
number 95 - 100 -> Blackjack
number 58 - 94 -> Win
number 49 - 57 -> Push
number < 49 -> Lose
"""

def bwpl():
    num = random.randint(1, 100)
    if num > 95:
        return 'b'
    elif num > 58:
        return 'w'
    elif num > 49:
        return 'p'
    else:
        return 'l'

print(bwpl())