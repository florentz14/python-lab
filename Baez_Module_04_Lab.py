# -------------------------------------------------
# File Name: Baez_Module_04_Lab.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
# Date: Module 04 Lab
# Description: Programming exercises including:
#              1. Average Rainfall
#              2. Ocean Levels
#              3. Tuition Increase
#              4. Population
# -------------------------------------------------

# =============================================================================
# EXERCISE 1: Average Rainfall
# =============================================================================
# Description: Write a program that uses nested loops to collect data and 
#              calculate the average rainfall over a period of years. The program 
#              should first ask for the number of years. The outer loop will 
#              iterate once for each year. The inner loop will iterate twelve 
#              times, once for each month. Each iteration of the inner loop 
#              will ask the user for the inches of rainfall for that month. 
#              After all iterations, the program should display the number of 
#              months, the total inches of rainfall, and the average rainfall 
#              per month for the entire period.
# =============================================================================

print("=" * 60)
print("EXERCISE 1: Average Rainfall")
print("=" * 60)

# Get number of years
# Try-except block: Handles exceptions that may occur during input conversion
try:
    num_years = int(input("Enter the number of years: "))
    
    if num_years < 1:
        print("Error: Number of years must be at least 1.")
    else:
        # Initialize variables
        total_rainfall = 0.0
        total_months = 0
        
        # Outer loop (for): Iterates for each year from 1 to num_years
        for year in range(1, num_years + 1):
            print(f"\nYear {year}:")
            # Inner loop (for): Iterates for each month (12 months in a year)
            for month in range(1, 13):
                month_names = ["", "January", "February", "March", "April", "May", "June",
                              "July", "August", "September", "October", "November", "December"]
                
                # Loop (while True): Continuously prompts until valid rainfall input is provided
                while True:
                    # Try-except block: Handles exceptions during rainfall input conversion
                    try:
                        rainfall = float(input(f"  Enter inches of rainfall for {month_names[month]}: "))
                        if rainfall < 0:
                            print("    Error: Rainfall cannot be negative. Please try again.")
                            continue  # Continue loop to ask for input again
                        total_rainfall += rainfall  # Accumulate total rainfall
                        total_months += 1  # Increment month counter
                        break  # Exit the while loop when valid input is processed
                    except ValueError:
                        # Handle invalid numeric input (e.g., non-numeric characters)
                        print("    Error: Please enter a valid number.")
        
        # Calculate average
        average_rainfall = total_rainfall / total_months if total_months > 0 else 0
        
        # Display results
        print("\n" + "=" * 60)
        print("RAINFALL SUMMARY")
        print("=" * 60)
        print(f"Number of months: {total_months}")
        print(f"Total inches of rainfall: {total_rainfall:.2f}")
        print(f"Average rainfall per month: {average_rainfall:.2f} inches")
        
except ValueError:
    # Handle invalid numeric input (e.g., non-numeric characters)
    print("Error: Please enter a valid integer for the number of years.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 2: Ocean Levels
# =============================================================================
# Description: Assuming the ocean's level is currently rising at about 1.6 
#              millimeters per year, write a program that displays a table 
#              showing the number of millimeters that the ocean will have risen 
#              each year for the next 25 years.
# =============================================================================

print("=" * 60)
print("EXERCISE 2: Ocean Levels")
print("=" * 60)

# Constants
RISE_RATE = 1.6  # millimeters per year
YEARS_TO_DISPLAY = 25

print(f"Assuming the ocean's level is rising at {RISE_RATE} millimeters per year:")
print(f"\nYear\t\tOcean Level Rise (mm)")
print("-" * 40)

# Loop (for): Iterates through each year from 1 to 25 to calculate and display ocean level rise
for year in range(1, YEARS_TO_DISPLAY + 1):
    total_rise = RISE_RATE * year  # Calculate cumulative rise for the year
    print(f"{year}\t\t{total_rise:.1f}")

print(f"\nAfter {YEARS_TO_DISPLAY} years, the ocean will have risen {RISE_RATE * YEARS_TO_DISPLAY:.1f} millimeters.")
print()

# =============================================================================
# EXERCISE 3: Tuition Increase
# =============================================================================
# Description: At one college, the tuition for a full-time student is $8,000 
#              per semester. It has been announced that the tuition will 
#              increase by 3 percent each year for the next 5 years. Write a 
#              program with a loop that displays the projected semester tuition 
#              amount for the next 5 years.
# =============================================================================

print("=" * 60)
print("EXERCISE 3: Tuition Increase")
print("=" * 60)

# Constants
CURRENT_TUITION = 8000  # dollars per semester
INCREASE_RATE = 0.03  # 3 percent
YEARS = 5

print(f"Current tuition: ${CURRENT_TUITION:,.2f} per semester")
print(f"Annual increase rate: {INCREASE_RATE * 100}%")
print(f"\nProjected semester tuition for the next {YEARS} years:")
print(f"\nYear\t\tTuition per Semester")
print("-" * 40)

# Calculate and display tuition for next 5 years
tuition = CURRENT_TUITION
# Loop (for): Iterates through each year from 1 to 5 to calculate and display projected tuition
for year in range(1, YEARS + 1):
    print(f"{year}\t\t${tuition:,.2f}")
    tuition = tuition * (1 + INCREASE_RATE)  # Increase by 3% each year (compound interest)

print()

# =============================================================================
# EXERCISE 4: Population
# =============================================================================
# Description: Write a program that predicts the approximate size of a 
#              population of organisms. The application should use text boxes 
#              to allow the user to enter the starting number of organisms, the 
#              average daily population increase (as a percentage), and the 
#              number of days the organisms will be left to multiply. For 
#              example, assume the user enters the following values:
#              • Starting number of organisms: 2
#              • Average daily increase: 30%
#              • Number of days to multiply: 10
#              The program should display a table showing the day number and the 
#              population at the beginning of that day.
# =============================================================================

print("=" * 60)
print("EXERCISE 4: Population")
print("=" * 60)

# Get user input
# Try-except block: Handles exceptions that may occur during input conversion
try:
    starting_population = float(input("Enter the starting number of organisms: "))
    
    if starting_population < 2:
        print("Error: Starting population must be at least 2.")
    else:
        daily_increase = float(input("Enter the average daily population increase (as a percentage): "))
        
        if daily_increase < 0:
            print("Error: Daily increase cannot be negative.")
        else:
            num_days = int(input("Enter the number of days the organisms will be left to multiply: "))
            
            if num_days < 1:
                print("Error: Number of days must be at least 1.")
            else:
                # Convert percentage to decimal
                increase_rate = daily_increase / 100
                
                # Calculate and display population for each day
                print(f"\nDay\t\tPopulation")
                print("-" * 40)
                
                population = starting_population
                print(f"0\t\t{population:,.2f}")  # Display starting population
                
                # Loop (for): Iterates through each day to calculate and display population growth
                for day in range(1, num_days + 1):
                    population = population * (1 + increase_rate)  # Apply exponential growth formula
                    print(f"{day}\t\t{population:,.2f}")
                
                print(f"\nStarting population: {starting_population:,.2f}")
                print(f"Daily increase: {daily_increase}%")
                print(f"Final population after {num_days} days: {population:,.2f}")
                
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
print("1. Average Rainfall Calculation: Standard statistical formula for average")
print("2. Ocean Level Rise: Based on scientific measurements")
print("   Source: NOAA - Sea Level Rise")
print("   https://oceanservice.noaa.gov/facts/sealevel.html")
print("3. Tuition Increase Calculation: Compound interest formula")
print("   Formula: Future Value = Present Value × (1 + rate)^years")
print("4. Population Growth: Exponential growth model")
print("   Formula: Population = Starting Population × (1 + growth rate)^days")
print("   Source: Population Growth Models - Exponential Growth")
print("   https://en.wikipedia.org/wiki/Exponential_growth")
