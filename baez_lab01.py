# -------------------------------------------------
# File Name: baez_lab01.py
# Author: Florentino Báez
# Date: August 16, 2025
# Description: This program calculates weekly expenses
#              and displays the remaining budget.
# -------------------------------------------------

# -------------------------
# 1. Store information in variables
# -------------------------

# Store the author's name
name = "Florentino Báez"

# Weekly budget
weekly_budget = 500

# Expenses
groceries = 25
rent = 25
electricity = 100
gas = 100
entertainment = 75  # New expense variable

# -------------------------
# 2. Perform calculations
# -------------------------

# Calculate total expenses
total_expenses = groceries + rent + electricity + gas + entertainment

# Calculate remaining money
money_left = weekly_budget - total_expenses

# -------------------------
# 3. Display results
# -------------------------

print("Hello, my name is", name)
print("My weekly budget is $", weekly_budget)
print("This week I spent a total of $", total_expenses)

print("I spent $", groceries, "on groceries.")
print("I spent $", rent, "on rent.")
print("I spent $", electricity, "on electricity.")
print("I spent $", gas, "on gas.")
print("I spent $", entertainment, "on entertainment.")

print("I have $", money_left, "left at the end of the week.")

# -------------------------
# 4. Check if overspent or saved money
# -------------------------

if money_left < 0:
    print("\nWARNING: I overspent by $", abs(money_left))
elif money_left > 0:
    print("\nGreat! I saved $", money_left, "this week.")
else:
    print("\nI spent exactly my budget. No money left, but no overspending.")
