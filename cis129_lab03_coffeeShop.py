"""

File: coffeeshop.py
Author: Gary Reisinger
Date: 10/2/2024
Description: This is a simple script I made meant to function as a coffee shop
It asks the user how many coffees/muffins they'd like to buy, and calculated the total
based on the pre established price and tax rate

"""

# Establishes price of coffee, muffins, and the tax rate

coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06

print('***************************************')
print('My Coffee and Muffin Shop')

# Get user imput for number of coffee and muffins bought

coffee_num =  int(input('Number of coffees bought?\n'))
muffin_num = int(input('Number of muffins bought?\n'))

# Calculates total

coffee_total = coffee_num * coffee_price
muffin_total = muffin_num * muffin_price
subtotal = coffee_total + muffin_total
tax = subtotal * tax_rate
total = subtotal + tax

# Establishes singular or plural for coffee and muffins bought

coffee_label = "Coffee"
if coffee_num != 1:
    coffee_label = "Coffees"
    
muffin_label = "Muffin"
if muffin_num != 1:
    muffin_label = "Muffins"

# prints out the number of coffees/muffins bought as well as their combined price + tax

print('***************************************\n')
print('***************************************')
print('My Coffee and Muffin Shop Receipt')
print(str(coffee_num) + ' ' + coffee_label + ' at $' + str(coffee_price) + ' each: $ ' + str(coffee_total))
print(str(muffin_num) + ' ' + muffin_label + ' at $' + str(muffin_price) + ' each: $ ' + str(muffin_total))
print('6% tax: $' + str(tax))
print('---------')
print('Total: $ ' + str(total))
print('***************************************')
