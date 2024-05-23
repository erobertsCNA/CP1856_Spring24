# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:31:17 2024

@author: Arun.Rameshbabu
"""

"""
Algorithm

print statement for the title with appropriate formatting

print statement for 999 input
print decorator
intitate variables
start a while loop
    get input
    check if input is within the prescribed value. if check passes
        convert into integer
        add it to sum
        increment counter
    check if input is 999
        break / update the check variable
    otherwise
        print the error message
print a decorator
print total score, avg score, newline and Bye!
"""

print("The Test Scores program\n")
print("Enter 999 to end input")
print('='*40)

# Prepare variables
total_score = 0
counter_avg = 0
# temp_input = 0 # Uncomment for loop structure 1

# Loop structure
# while (temp_input != '999'):
#     temp_input = input("Enter test score: ")
#     if temp_input == '999':
#         pass
#     elif (int(temp_input) >= 0) and (int(temp_input) <= 100):
#         total_score += int(temp_input)
#         counter_avg += 1
#     else:
#         print("Test score must be from 0 through 100. Try again.")

# Alternate Loop Structure
while True:
    temp_input = input("Enter test score: ")
    if temp_input == '999':
        break
    elif (int(temp_input) >= 0) and (int(temp_input) <= 100):
        total_score += int(temp_input)
        counter_avg += 1
    else:
        print("Test score must be from 0 through 100. Try again.")

print('='*40)
print(f"Total Score: {total_score}")
print(f"Average Score: {(total_score / counter_avg):.0f}")
print("\nBye!")
        