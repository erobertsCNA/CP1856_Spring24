# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:39:01 2024

@author: Arun.Rameshbabu
"""

print("SALES DATA IMPORTER\n")
print("Enter sales data\n")
amount = float(input("Amount:\t\t\t"))
year = int(input("Year:\t\t\t"))
month = int(input("Month (1-12):\t"))
day = int(input("Day (1-31):\t\t"))

print(f"\n1.\t\t\t\t{year}-{month}-{day}\t\t${amount:.1f}\n")
total_amount = 0
total_amount += amount

amount = float(input("Amount:\t\t\t"))
year = int(input("Year:\t\t\t"))
month = int(input("Month (1-12):\t"))
day = int(input("Day (1-31):\t\t"))

print(f"\n2.\t\t\t\t{year}-{month}-{day}\t\t${amount:.1f}\n")
total_amount += amount

amount = float(input("Amount:\t\t\t"))
year = int(input("Year:\t\t\t"))
month = int(input("Month (1-12):\t"))
day = int(input("Day (1-31):\t\t"))

print(f"\n3.\t\t\t\t{year}-{month}-{day}\t\t${amount:.1f}\n")
total_amount += amount

print("Total Sales")
print("-----------")
print(f"${total_amount:.1f}\n")
print("Bye!")
