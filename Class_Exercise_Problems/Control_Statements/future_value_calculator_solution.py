# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:53:24 2024

@author: Arun.Rameshbabu
"""

"""
Algorithm

Print welcome message
Get the inputs

Calculate the monthly interest rate = yearly / 12
Calculate the number of months = years * 12

run a for loop for the range(number of months)
    add the monhly contribution
    calculate the monthly interest
    add the monthly interest to the final sum (future value)

print final sum (future value)
"""

print("Welcome to the Future Value Calculator\n")
choice = 'y'
while choice.lower() == 'y':
    
    # Gathering inputs
    monthly_investment = float(input("Enter monthly investment:\t\t"))
    intrest_rate_yr = float(input("Enter yearly interest rate:\t\t"))
    num_years = float(input("Enter the number of years:\t\t"))
    
    # Do the calculations
    future_value = 0
    interest_rate_monthly = (intrest_rate_yr/12)/100
    num_months = num_years * 12
    
    # Loop through
    for mnth in range(int(num_months)):
        future_value += monthly_investment # Add new investment
        interest_for_mnth = future_value * interest_rate_monthly # Calculate interest for month
        future_value += interest_for_mnth # Add interest to the principal
    
    # Print the outputs
    print(f"Future Value:\t\t\t\t\t{future_value:.2f}\n")
    choice = input("Continue (y/n)?:")
