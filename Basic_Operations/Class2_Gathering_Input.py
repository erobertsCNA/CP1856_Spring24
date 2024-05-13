# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:32:47 2024

@author: Arun.Rameshbabu
"""

"""
Change between types
"""
test = 10
str_test = str(test)

print("I am going to put " + str(test))

str_number = '35.5'
#int_number = int(str_number)
flt_number = float(str_number)


"""
Gathering input from user
"""
"""
Write the code to calculate the sales tax for the province of NL
Gather input from the user for:  
    Sale total before tax
    Tax rate
"""
# input()
sales_total = input("Enter sale total before tax: ")
sales_total = int(sales_total)
tax_rate = float(input("Enter tax rate: ")) / 100
sales_tax = sales_total * tax_rate
print("The sales tax is: ", end='')
print(sales_tax, end=' $\n')

print("The sales tax is: $ {}".format(sales_tax))

print(f"The sales tax is: $ {sales_tax}")

"""
Write the code to calculate the perimeter and the area of a rectangle
Gather input from the user for: 
    Side a
    Side b 
"""
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
area = side_a * side_b
perimeter = (2 * side_a) + (2 * side_b)

print(f"The area of the rectangle given side a as {side_a} and side b as {side_b} is {area} and the perimeter is {perimeter}")