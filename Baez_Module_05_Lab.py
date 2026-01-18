# -------------------------------------------------
# File Name: Baez_Module_05_Lab.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
# Date: Module 05 Lab
# Description: Programming exercises including:
#              1. Calories from Fat and Carbohydrates
#              2. Monthly Sales Tax
#              3. Test Average and Grade
#              4. Prime Numbers
# -------------------------------------------------

# =============================================================================
# EXERCISE 1: Calories from Fat and Carbohydrates
# =============================================================================
# Description: A nutritionist who works for a fitness club helps members by 
#              evaluating their diets. As part of her evaluation, she asked 
#              members how many fat grams and carbohydrate grams they consumed 
#              in a day. Then, she calculates the number of calories that 
#              result from the fat, using the following formula:
#
#              calories from fat = fat grams x 9
#
#              Next, she calculates the number of calories that result from 
#              the carbohydrates, using the following formula:
#
#              calories from carbs = carb grams x 4
#
#              The nutritionist asks you to write a program that will make 
#              these calculations.
# =============================================================================

def calculate_calories_from_fat(fat_grams):
    """
    Calculate calories from fat.
    
    Args:
        fat_grams (float): Number of fat grams consumed
        
    Returns:
        float: Number of calories from fat (fat_grams x 9)
    """
    return fat_grams * 9


def calculate_calories_from_carbs(carb_grams):
    """
    Calculate calories from carbohydrates.
    
    Args:
        carb_grams (float): Number of carbohydrate grams consumed
        
    Returns:
        float: Number of calories from carbohydrates (carb_grams x 4)
    """
    return carb_grams * 4


print("=" * 60)
print("EXERCISE 1: Calories from Fat and Carbohydrates")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    fat_grams = float(input("Enter the number of fat grams consumed: "))
    carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))
    
    # Validate inputs
    if fat_grams < 0 or carb_grams < 0:
        print("Error: Fat grams and carbohydrate grams must be non-negative.")
    else:
        # Calculate calories using functions
        calories_from_fat = calculate_calories_from_fat(fat_grams)
        calories_from_carbs = calculate_calories_from_carbs(carb_grams)
        total_calories = calories_from_fat + calories_from_carbs
        
        # Display results
        print(f"\nCalories from fat: {calories_from_fat:.2f}")
        print(f"Calories from carbohydrates: {calories_from_carbs:.2f}")
        print(f"Total calories: {total_calories:.2f}")
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter valid numbers.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 2: Monthly Sales Tax
# =============================================================================
# Description: A retail company must file a monthly sales tax report listing 
#              the total sales for the month, and the amount of state and 
#              county sales tax collected. The state sales tax rate is 5 percent 
#              and the county sales tax rate is 2.5 percent. Write a program 
#              that asks the user to enter the total sales for the month. From 
#              this figure, the application should calculate and display the 
#              following:
#              • The amount of county sales tax
#              • The amount of state sales tax
#              • The total sales tax (county plus state)
# =============================================================================

def calculate_county_sales_tax(total_sales, county_rate=0.025):
    """
    Calculate county sales tax.
    
    Args:
        total_sales (float): Total sales for the month
        county_rate (float): County sales tax rate (default 0.025 for 2.5%)
        
    Returns:
        float: Amount of county sales tax
    """
    return total_sales * county_rate


def calculate_state_sales_tax(total_sales, state_rate=0.05):
    """
    Calculate state sales tax.
    
    Args:
        total_sales (float): Total sales for the month
        state_rate (float): State sales tax rate (default 0.05 for 5%)
        
    Returns:
        float: Amount of state sales tax
    """
    return total_sales * state_rate


def calculate_total_sales_tax(total_sales, county_rate=0.025, state_rate=0.05):
    """
    Calculate total sales tax (county + state).
    
    Args:
        total_sales (float): Total sales for the month
        county_rate (float): County sales tax rate (default 0.025 for 2.5%)
        state_rate (float): State sales tax rate (default 0.05 for 5%)
        
    Returns:
        float: Total sales tax amount
    """
    county_tax = calculate_county_sales_tax(total_sales, county_rate)
    state_tax = calculate_state_sales_tax(total_sales, state_rate)
    return county_tax + state_tax


print("=" * 60)
print("EXERCISE 2: Monthly Sales Tax")
print("=" * 60)

# Constants
STATE_TAX_RATE = 0.05  # 5 percent
COUNTY_TAX_RATE = 0.025  # 2.5 percent

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    total_sales = float(input("Enter the total sales for the month: $"))
    
    # Validate input
    if total_sales < 0:
        print("Error: Total sales cannot be negative.")
    else:
        # Calculate taxes using functions
        county_tax = calculate_county_sales_tax(total_sales, COUNTY_TAX_RATE)
        state_tax = calculate_state_sales_tax(total_sales, STATE_TAX_RATE)
        total_tax = calculate_total_sales_tax(total_sales, COUNTY_TAX_RATE, STATE_TAX_RATE)
        
        # Display results
        print(f"\nTotal Sales: ${total_sales:,.2f}")
        print(f"County Sales Tax ({COUNTY_TAX_RATE * 100}%): ${county_tax:,.2f}")
        print(f"State Sales Tax ({STATE_TAX_RATE * 100}%): ${state_tax:,.2f}")
        print(f"Total Sales Tax: ${total_tax:,.2f}")
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter a valid number.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 3: Test Average and Grade
# =============================================================================
# Description: Write a program that asks the user to enter five test scores. 
#              The program should display a letter grade for each score and the 
#              average test score. Write the following functions in the program:
#              • calc_average. This function should accept five test scores as 
#                arguments and return the average of the scores.
#              • determine_grade. This function should accept a test score as 
#                an argument and return a letter grade for the score based on 
#                the following grading scale:
#
#                Score                 Letter Grade
#                90–100                   A
#                80–89                     B
#                70–79                     C
#                60–69                     D
#                Below 60                F
# =============================================================================

def calc_average(score1, score2, score3, score4, score5):
    """
    Calculate the average of five test scores.
    
    Args:
        score1 (float): First test score
        score2 (float): Second test score
        score3 (float): Third test score
        score4 (float): Fourth test score
        score5 (float): Fifth test score
        
    Returns:
        float: Average of the five test scores
    """
    return (score1 + score2 + score3 + score4 + score5) / 5


def determine_grade(score):
    """
    Determine the letter grade for a test score.
    
    Args:
        score (float): Test score
        
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print("=" * 60)
print("EXERCISE 3: Test Average and Grade")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    score1 = float(input("Enter test score 1: "))
    score2 = float(input("Enter test score 2: "))
    score3 = float(input("Enter test score 3: "))
    score4 = float(input("Enter test score 4: "))
    score5 = float(input("Enter test score 5: "))
    
    # Validate inputs
    scores = [score1, score2, score3, score4, score5]
    if any(score < 0 or score > 100 for score in scores):
        print("Error: Test scores must be between 0 and 100.")
    else:
        # Calculate average using function
        average = calc_average(score1, score2, score3, score4, score5)
        
        # Display results
        print(f"\nTest Score\t\tLetter Grade")
        print("-" * 40)
        print(f"Score 1: {score1:.2f}\t\t{determine_grade(score1)}")
        print(f"Score 2: {score2:.2f}\t\t{determine_grade(score2)}")
        print(f"Score 3: {score3:.2f}\t\t{determine_grade(score3)}")
        print(f"Score 4: {score4:.2f}\t\t{determine_grade(score4)}")
        print(f"Score 5: {score5:.2f}\t\t{determine_grade(score5)}")
        print("-" * 40)
        print(f"Average Score: {average:.2f}\t\t{determine_grade(average)}")
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter valid numbers.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 4: Prime Numbers
# =============================================================================
# Description: A prime number is a number that is only evenly divisible by 
#              itself and 1. For example, 5 is prime because it can only be 
#              evenly divided by 1 and 5. The number 6, however, is not prime 
#              because it can be divided evenly by 1, 2, 3, and 6. Write a 
#              Boolean function named is_prime which takes an integer as an 
#              argument and returns true if the argument is a prime number, or 
#              false otherwise. Use the function in a program that prompts the 
#              user to enter a number and then displays a message indicating 
#              whether the number is prime.
# =============================================================================

def is_prime(number):
    """
    Determine if a number is prime.
    
    A prime number is a number that is only evenly divisible by itself and 1.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # Check for divisibility from 2 to the square root of the number
    # If number is divisible by any number in this range, it's not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    # If no divisors found, the number is prime
    return True


print("=" * 60)
print("EXERCISE 4: Prime Numbers")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    number = int(input("Enter a number to check if it is prime: "))
    
    # Check if number is prime using function
    if is_prime(number):
        print(f"\n{number} is a prime number.")
    else:
        print(f"\n{number} is not a prime number.")
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter a valid integer.")
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
print("1. Calories Calculation:")
print("   - Fat: 1 gram of fat = 9 calories")
print("   - Carbohydrates: 1 gram of carbohydrates = 4 calories")
print("   Source: USDA National Nutrient Database")
print("   https://www.nal.usda.gov/fnic/how-many-calories-are-one-gram-fat-carbohydrate-or-protein")
print()
print("2. Sales Tax Calculation:")
print("   - Standard formula: Tax Amount = Sales Amount × Tax Rate")
print("   Source: State and Local Sales Tax Rates")
print("   https://taxfoundation.org/state-and-local-sales-tax-rates/")
print()
print("3. Grade Calculation:")
print("   - Standard letter grade scale (A-F)")
print("   Source: Common grading scale used in educational institutions")
print()
print("4. Prime Number Algorithm:")
print("   - Trial division method: Check divisibility from 2 to √n")
print("   Source: Prime Number - Wikipedia")
print("   https://en.wikipedia.org/wiki/Prime_number")
