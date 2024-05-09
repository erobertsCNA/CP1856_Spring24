# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:37:04 2024

@author: Arun.Rameshbabu
"""

"""
Python Airthmetic Operators
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor (Integer) Division
%   Modulus / Modulo / Remainder
**  Exponential (To the power of)
"""

add_example = 7 + 9.5
sub_example = 7 - 9
mul_example = 2 * 3
div_example = 8 / 3
flr_div = 8 // 3
mod_example = 7 % 3
exp_example = 2 ** 3

2 * (7 + 3) 

"""
Write the code to calculate the sales tax for the province of NL
Given:  
    Sale total before tax = 200
    Tax rate = 15 %
"""
sales_total = 200
tax_rate = 15 / 100
sales_tax = sales_total * tax_rate
print("The sales tax is: ", end='')
print(sales_tax, end=' $\n')

print("The sales tax is: $ {}".format(sales_tax))

print(f"The sales tax is: $ {sales_tax}")


"""
Write the code to calculate the perimeter and the area of a rectangle
Given:
    Side a = 10
    Side b = 20
"""
side_a = 10
side_b = 20
area = side_a * side_b
perimeter = (2 * side_a) + (2 * side_b)

print(f"The area of the rectangle is {area} and the perimeter is {perimeter}")

