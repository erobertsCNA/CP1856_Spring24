# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:40:02 2024

@author: Arun.Rameshbabu
"""

print("BLACKJACK!")
print("Blackjack payout is 3:2\n")

# Get the inputs
starting_money = float(input("Starting money:\t\t"))
bet_amount = float(input("Bet amount:\t\t\t"))

# Run the calculations
blackjack_amt = starting_money + (bet_amount * 1.5)
win_amt = starting_money + bet_amount
lose_amt = starting_money - bet_amount

# Display the output as required
print("\nENDING MONEY FOR A...")
print(f"Blackjack:\t\t\t{blackjack_amt}")
print(f"Win:\t\t\t\t{win_amt}")
print(f"Push:\t\t\t\t{starting_money}")
print(f"Lose:\t\t\t\t{lose_amt}")
print("\nBye!")
