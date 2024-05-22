# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:36:28 2024

@author: Arun.Rameshbabu
"""

print("The Invoice program\n")
customer_type = input("Enter customer type(r/w):\t")
invoice_total = float(input("Enter invoice total:\t\t"))

# Doing our calculations
# Check customer type
if customer_type.lower() == 'r':
    if invoice_total > 0 and invoice_total < 100:
        discount_percent = 0
    elif invoice_total > 0 and invoice_total < 250:
        discount_percent = 0.1
    elif invoice_total > 0 and invoice_total >= 250:
        discount_percent = 0.2
    else:
        discount_percent = 0
        print("Invalid invoice total. Please enter again")
elif customer_type.lower() == 'w':
    if invoice_total > 0 and invoice_total < 500:
        discount_percent = 0.4
    elif invoice_total > 0 and invoice_total >= 500:
        discount_percent = 0.5
    else:
        discount_percent = 0
        print("Invalid invoice total. Please enter again")

# Get the numbers
discount_amount = invoice_total * discount_percent
new_invoice_total = invoice_total - discount_amount

# Print them out, in the required format
print(f"\nInvoice total:\t\t\t{invoice_total:.1f}")
print(f"Discount percent:\t\t{discount_percent:.1f}")
print(f"Discount amount:\t\t{discount_amount:.1f}")
print(f"New invoice total:\t\t{new_invoice_total:.1f}")
