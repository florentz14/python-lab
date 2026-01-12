# -------------------------------------------------
# File Name: Baez_Module_03_Lab.py
# Author: Florentino Báez
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

print("=" * 60)
print("EXERCISE 1: Roman Numeral Converter")
print("=" * 60)

# Get user input with validation
while True:
    try:
        number = int(input("Enter a number within the range of 1 through 10: "))
        
        # Input validation: Do not accept a number less than 1 or greater than 10
        if number < 1 or number > 10:
            print("Error: Please enter a number between 1 and 10.")
            continue
        
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
        break
        
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 2: Magic Dates
# =============================================================================

print("=" * 60)
print("EXERCISE 2: Magic Dates")
print("=" * 60)

# Get user input
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
    print("Error: Please enter valid integers.")
except Exception as e:
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 3: February Days (Leap Year)
# =============================================================================

print("=" * 60)
print("EXERCISE 3: February Days (Leap Year)")
print("=" * 60)

# Get user input
try:
    year = int(input("Enter a year: "))
    
    # Determine if it's a leap year
    # Criteria:
    # 1. If divisible by 100, then it's a leap year if and only if also divisible by 400
    # 2. If not divisible by 100, then it's a leap year if and only if divisible by 4
    
    is_leap_year = False
    
    if year % 100 == 0:
        # Divisible by 100
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        # Not divisible by 100
        if year % 4 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    
    # Display the number of days in February
    if is_leap_year:
        days_in_february = 29
        print(f"In {year} February had {days_in_february} days.")
        print(f"{year} is a leap year.")
    else:
        days_in_february = 28
        print(f"In {year} February had {days_in_february} days.")
        print(f"{year} is not a leap year.")
        
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 4: Body Mass Index (BMI)
# =============================================================================

print("=" * 60)
print("EXERCISE 4: Body Mass Index (BMI)")
print("=" * 60)

# Get user input
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
            status = "underweight"
        elif 18.5 <= bmi <= 25:
            status = "optimal weight"
        else:  # bmi > 25
            status = "overweight"
        
        # Display results
        print(f"\nYour BMI: {bmi:.2f}")
        print(f"Weight Status: You have {status}.")
        
        # Display BMI ranges for reference
        print("\nBMI Ranges:")
        print("  Less than 18.5  - Underweight")
        print("  18.5 to 25      - Optimal weight")
        print("  Greater than 25 - Overweight")
        
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
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
