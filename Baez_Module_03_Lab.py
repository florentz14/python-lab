# -------------------------------------------------
# File Name: Baez_Module_03_Lab.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
# Date: Module 03 Lab
# Description: Programming exercises including:
#              1. Roman Numeral Converter
#              2. Magic Dates
#              3. February Days (Leap Year)
#              4. Body Mass Index (BMI)
# 
# Note: This file can be run directly or used in Jupyter Notebook
# -------------------------------------------------

# =============================================================================
# EXERCISE 1: Roman Numeral Converter
# =============================================================================
# Description: Write a program that asks the user to enter a number within the 
#              range of 1 through 10. The program should display the Roman 
#              numeral version of that number. If the number is outside the 
#              range of 1 through 10, the program should display an error 
#              message.
# =============================================================================

print("=" * 60)
print("EXERCISE 1: Roman Numeral Converter")
print("=" * 60)

# Get user input with validation
# Loop (while True): Continuously prompts the user until valid input is provided
while True:
    # Try-except block: Handles exceptions that may occur during input conversion
    try:
        number = int(input("Enter a number within the range of 1 through 10: "))
        
        # Input validation: Do not accept a number less than 1 or greater than 10
        if number < 1 or number > 10:
            print("Error: Please enter a number between 1 and 10.")
            continue  # Continue loop to ask for input again
        
        # Convert to Roman numeral using if-elif statements
        if number == 1:
            roman_numeral = "I"
        elif number == 2:
            roman_numeral = "II"
        elif number == 3:
            roman_numeral = "III"
        elif number == 4:
            roman_numeral = "IV"
        elif number == 5:
            roman_numeral = "V"
        elif number == 6:
            roman_numeral = "VI"
        elif number == 7:
            roman_numeral = "VII"
        elif number == 8:
            roman_numeral = "VIII"
        elif number == 9:
            roman_numeral = "IX"
        else:  # number == 10
            roman_numeral = "X"
        
        print(f"The Roman numeral version of {number} is: {roman_numeral}")
        break  # Exit the loop when valid input is processed
        
    except ValueError:
        # Handle invalid numeric input (e.g., non-numeric characters)
        print("Error: Please enter a valid integer.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 2: Magic Dates
# =============================================================================
# Description: The date June 10, 1960, is special because when we write it in 
#              the following format, the month times the day equals the year:
#              6/10/60. Write a program that asks the user to enter a month 
#              (in numeric form), a day, and a two-digit year. The program 
#              should then determine whether the month times the day equals the 
#              year. If so, it should display a message saying the date is 
#              magic. Otherwise, it should display a message saying the date is 
#              not magic.
# =============================================================================

print("=" * 60)
print("EXERCISE 2: Magic Dates")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    month = int(input("Enter a month (in numeric form, 1-12): "))
    day = int(input("Enter a day: "))
    year = int(input("Enter a two-digit year: "))
    
    # Check if the date is magic
    # A date is magic if month * day equals the year
    if month * day == year:
        print(f"\nThe date {month}/{day}/{year:02d} is a MAGIC DATE!")
        print(f"Because {month} x {day} = {month * day}, which equals the year {year:02d}")
    else:
        print(f"\nThe date {month}/{day}/{year:02d} is NOT a magic date.")
        print(f"Because {month} x {day} = {month * day}, which does not equal the year {year:02d}")
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter valid integers.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 3: February Days (Leap Year)
# =============================================================================
# Description: The month of February normally has 28 days. But if it is a leap 
#              year, February has 29 days. Write a program that asks the user 
#              to enter a year. The program should then display the number of 
#              days in February that year. Use the following criteria to 
#              identify leap years:
#              • If the year is divisible by 100, then it is a leap year if 
#                and only if it is also divisible by 400.
#              • If the year is not divisible by 100, then it is a leap year 
#                if and only if it is divisible by 4.
# =============================================================================

print("=" * 60)
print("EXERCISE 3: February Days (Leap Year)")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    year = int(input("Enter a year: "))
    
    # Determine if it's a leap year
    # Criteria:
    # 1. If divisible by 100, then it's a leap year if and only if also divisible by 400
    # 2. If not divisible by 100, then it's a leap year if and only if divisible by 4
    
    is_leap_year = False # Initialize is_leap_year to False
    
    if year % 100 == 0:
        # Divisible by 100
        if year % 400 == 0:
            is_leap_year = True # Set is_leap_year to True if year is divisible by 100 and 400
        else:
            is_leap_year = False # Set is_leap_year to False if year is not divisible by 100 and 400
    else:
        # Not divisible by 100
        if year % 4 == 0:
            is_leap_year = True # Set is_leap_year to True if year is not divisible by 100 and 4
        else:
            is_leap_year = False # Set is_leap_year to False if year is not divisible by 100 and 4
    
    # Display the number of days in February
    if is_leap_year:
        days_in_february = 29 # Set days_in_february to 29 if year is a leap year
        print(f"In {year} February had {days_in_february} days.")
        print(f"{year} is a leap year.")
    else:
        days_in_february = 28 # Set days_in_february to 28 if year is not a leap year
        print(f"In {year} February had {days_in_february} days.")
        print(f"{year} is not a leap year.")
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter a valid integer.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 4: Body Mass Index (BMI)
# =============================================================================
# Description: Write a program that calculates and displays a person's Body Mass 
#              Index (BMI). The BMI is often used to determine whether a person 
#              is underweight, optimal weight, or overweight for their height. 
#              The program should ask the user to enter their weight in pounds 
#              and height in inches, then calculate and display their BMI. The 
#              program should also display a message indicating whether the 
#              person has optimal weight, is underweight, or is overweight. A 
#              person's BMI is calculated with the following formula:
#
#              BMI = weight x 703 / height^2
#
#              Where weight is measured in pounds and height is measured in 
#              inches. A person's weight status is determined as follows:
#              • BMI < 18.5: Underweight
#              • 18.5 ≤ BMI ≤ 25: Optimal weight
#              • BMI > 25: Overweight
# =============================================================================

print("=" * 60)
print("EXERCISE 4: Body Mass Index (BMI)")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    
    # Validate inputs
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
    else:
        # Calculate BMI
        # Formula: BMI = weight x 703 / height^2
        bmi = (weight * 703) / (height ** 2)
        
        # Determine weight status
        if bmi < 18.5:
            status = "underweight" # Set status to "underweight" if BMI is less than 18.5
        elif 18.5 <= bmi <= 25:
            status = "optimal weight" # Set status to "optimal weight" if BMI is between 18.5 and 25
        else:  # bmi > 25
            status = "overweight" # Set status to "overweight" if BMI is greater than 25
        
        # Display results
        print(f"\nYour BMI: {bmi:.2f}")
        print(f"Weight Status: You have {status}.")
        
        # Display BMI ranges for reference
        print("\nBMI Ranges:") # Display BMI ranges for reference   
        print("  Less than 18.5  - Underweight") # Display Underweight range
        print("  18.5 to 25      - Optimal weight") # Display Optimal weight range
        print("  Greater than 25 - Overweight") # Display Overweight range
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter valid numbers.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()
print("=" * 60)
print("All exercises completed!")
print("=" * 60)

# =============================================================================
# CITATIONS
# =============================================================================
print("\nCitations:")
print("1. Roman Numerals: Standard Roman numeral system (I, V, X)")
print("2. Leap Year Calculation: Gregorian calendar rules")
print("   Source: https://en.wikipedia.org/wiki/Leap_year")
print("3. BMI Calculation: CDC - Body Mass Index (BMI)")
print("   Formula: BMI = (weight in pounds x 703) / (height in inches)^2")
print("   Source: https://www.cdc.gov/healthyweight/assessing/bmi/index.html")
print("4. BMI Categories: CDC - About Adult BMI")
print("   Source: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html")
