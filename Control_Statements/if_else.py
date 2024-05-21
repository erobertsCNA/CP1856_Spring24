# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:40:13 2024

@author: Arun.Rameshbabu
"""

"""
Syntax of if else

if boolean_expression:
    statements....
elif boolean_expression_2:
    statements....
elif boolean_expression_3:
    statements....
else:
    statements....
"""

# age = 17
# if (age >= 18):
#     print("You may vote!")
# else:
#     print("Wait until you are 18 years old!")
    
"""
Conditions
>= 500 - Discount 20%
>= 250 < 500 Disccount 10%
> 0
"""
# invoice_total = 600
invoice_total = float(input("Enter invoice total: "))

if invoice_total >= 500:
    if invoice_total >= 500 and invoice_total < 750:
        discount_percent = 0.2
        print("Invoice total is more than 500. You get a 20% discount.")
    else:
        discount_percent = 0.3
        print("Invoice total is more than 500. You get a 30% discount.")
elif (invoice_total >= 250) and (invoice_total < 500):
    discount_percent = 0.1
    print("Invoice total is more than 250. You get a 10% discount. If you buy stuff worth atleast 500, you'll get a 20% discount!")
elif invoice_total > 0:
    discount_percent = 0
    print("Consider shopping for $ 250 to get a discount of 10%")
else:
    print("You need to buy something to generate an invoice!")
    discount_percent = 0

if discount_percent > 0:
    print(f"Discount: {invoice_total * discount_percent}")