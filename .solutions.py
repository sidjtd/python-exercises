# 1. As a valued customer at the Bank of Honolulu, you make a deposit of $1000. Your savings account balance prior to the deposit has an amount of $8000. Calculate the new savings account balance. Print the new savings account balance and concatenate the dollar sign.

current_balance = 8000
deposit = 1000
new_balance = current_balance + deposit
print('$' + str(new_balance))

# 2. You need to pay taxes on the $500 cash prize that you won to the IRS ( The tax rate is 30%). Calculate the tax amount and subtract this from your savings balance. Print the updated savings account balance and concatenate the dollar sign.

tax_rate = .30
prize = 500
tax_amount = prize * tax_rate
print(tax_amount)
updated_balance = new_balance - tax_amount
print('$' + str(updated_balance))

#3. The savings account accrues an annual interest rate of 2%. Calculate the interest earned for the first quarter of 2018, using the original account balance from Question 1. Print the interst earned in the first quarter and concatenate the dollar sign.

int_rate = .02
quarter_int_rate = int_rate / 4
int_earned = current_balance * quarter_int_rate 
print('$' + str(int_earned))

# 4. Function add
# Create a function that will take two parameters named num1 and num2. This function will add two numbers. Print your result.

def add(n1, n2):
    return n1 + n2
total = add(1,2)
print(total)

# 5. Function subtract
# Create a function that will take two parameters named num1 and num2. This function will subtract two numbers. Print your result.

def subtract(n1, n2):
    return n2 - n1
difference = subtract(3, 11)
print(difference)

# 6. Function add-then-subtract
# Create a function that will take in three parameters named num1, num2 and num3. The function will sum up the first two parameters (num1 and num2) and subtract it from the third parameter (num3). Please use your previous functions (i.e. add or subtract) for this exercise. Print your result.

def addThenSubtract(n1, n2, n3):
    return subtract(n3, add(n1, n2))
result = addThenSubtract(10, 6, 70)
print(result)

# 7. Function shoe size
#  Create a function that will take in a parameter named inches. This function will convert inches to centimeters(cm). Print your result. 

def shoe_size(inches):
    cm = inches * 2.54
    return cm
converion = shoe_size(11)
print(converion)

# 8. Create a function that will take in a parameter named cel. The function will convert Celsius into Fahrenheit. Print your result.

def converter(cel):
    faren = cel * 9/5 + 32
    return faren
print(converter(10))

# 9. Function all caps
#  Create a function that will take in a parameter named str. This function will capitalize all the letters in the string. Print your result. 

def all_caps(str):
    return str.upper()
print(all_caps('dog'))

# 10. Function one cap
#  Create a function that will take in a parameter named str. The function will capitalize only the first letter in the string. Print your result.

def one_cap(str):
    return str[0].upper() + str[1:]
print(one_cap('donut flavored oreos!'))

# 11. Use the extend method to combine the following lists together. Print your result.

east_side = ['Biggie', 'Nas', 'Wu-Tang Clan']
west_side = ['Tupac', 'Dre', 'Snoop']
east_side.extend(west_side)
print(east_side)

# 12. Use the clear method to remove all items from the following list. If you are using Python 2 or 3.2, use the del operator instead. Print your result.

haters = ['Keyshia Cole', 'Wendy Williams', '50 Cent', 'Lil Kim']
haters.clear()
print(haters)

# 13. Create a function that will print that last digit of an integer. 

def last_digit(num):
    print num % 10
last_digit(111)
