"""

File: coffeeshop.py
Author: Gary Reisinger
Date: 10/2/2024
Description: This is a simple script I made meant to function as a coffee shop
It asks the user how many coffees/muffins/bagels/donuts they'd like to buy
and calculated the total based on the pre established price and tax rate

"""

# Establishes price of coffee, muffins, and the tax rate

coffee_price = 5.00
bagel_price = 2.50
donut_price = 1.50
muffin_price = 4.00
tax_rate = 0.06

print('***************************************')
print('My Coffee, Muffin, Bagel, and Donut Shop')

# Get user imput for number of coffee and muffins bought

coffee_num =  int(input('Number of coffees bought?\n'))
muffin_num = int(input('Number of muffins bought?\n'))
bagel_num = int(input('Number of bagels bought?\n'))
donut_num = int(input('Number of donuts bought?\n'))

# Calculates total

coffee_total = coffee_num * coffee_price
muffin_total = muffin_num * muffin_price
bagel_total = bagel_num * bagel_price
donut_total = donut_num * donut_price
subtotal = coffee_total + muffin_total + bagel_total + donut_total
tax = round(subtotal * tax_rate, 2)
total = subtotal + tax

# Establishes singular or plural for items bought

coffee_label = "Coffee"
if coffee_num != 1:
    coffee_label = "Coffees"
    
muffin_label = "Muffin"
if muffin_num != 1:
    muffin_label = "Muffins"

bagel_label = "Bagel"
if bagel_num != 1:
    bagel_label = "Bagels"

donut_label = "Donut"
if donut_num != 1:
    donut_label = "Donuts"

# prints out the number of coffees/muffins bought as well as their combined price + tax

print('***************************************\n')
print('***************************************')
print('My Coffee, Muffin, Bagel, and Donut Shop Receipt')
print(str(coffee_num) + ' ' + coffee_label + ' at $' + str(coffee_price) + ' each: $ ' + str(coffee_total))
print(str(muffin_num) + ' ' + muffin_label + ' at $' + str(muffin_price) + ' each: $ ' + str(muffin_total))
print(str(bagel_num) + ' ' + bagel_label + ' at $' + str(bagel_price) + ' each: $ ' + str(bagel_total))
print(str(donut_num) + ' ' + donut_label + ' at $' + str(donut_price) + ' each: $ ' + str(donut_total))
print('6% tax: $' + str(tax))
print('---------')
print('Total: $ ' + str(total))
print('***************************************')
print('Thank you for using my script, I look forward to seeing you again!')
    
