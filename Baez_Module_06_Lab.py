# -------------------------------------------------
# File Name: Baez_Module_06_Lab.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
# Date: Module 06 Lab
# Description: Programming exercises including:
#              1. Number Analysis Program
#              2. Employees Pay Program
#              3. Exam Grades Program
# -------------------------------------------------

# =============================================================================
# EXERCISE 1: Number Analysis Program
# =============================================================================
# Description: Design a program that asks the user to enter a series of 20 
#              numbers. The program should store the numbers in a list, and 
#              then display the following data:
#              • The lowest number on the list
#              • The highest number on the list
#              • The total of the numbers in the list
#              • The average of the numbers in the list
# =============================================================================

print("=" * 60)
print("EXERCISE 1: Number Analysis Program")
print("=" * 60)

# Initialize list to store numbers
numbers = []

# Get 20 numbers from user
# Try-except block: Handles exceptions that may occur during input conversion
try:
    print("Enter 20 numbers:")
    for i in range(1, 21):
        # Loop (for): Iterates 20 times to collect numbers from user
        while True:
            # Loop (while True): Continuously prompts until valid number is provided
            try:
                number = float(input(f"  Enter number {i}: "))
                numbers.append(number)  # Add number to the list
                break  # Exit the while loop when valid input is processed
            except ValueError:
                # Handle invalid numeric input (e.g., non-numeric characters)
                print("    Error: Please enter a valid number.")
    
    # Calculate statistics
    if numbers:
        lowest_number = min(numbers)  # Find the lowest number in the list
        highest_number = max(numbers)  # Find the highest number in the list
        total = sum(numbers)  # Calculate the sum of all numbers
        average = total / len(numbers)  # Calculate the average
        
        # Display results
        print("\n" + "=" * 60)
        print("NUMBER ANALYSIS RESULTS")
        print("=" * 60)
        print(f"Lowest number: {lowest_number}")
        print(f"Highest number: {highest_number}")
        print(f"Total of all numbers: {total}")
        print(f"Average of all numbers: {average:.2f}")
    else:
        print("Error: No numbers were entered.")
        
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 2: Employees Pay Program
# =============================================================================
# Description: Megan owns a small neighborhood coffee shop with six employees 
#              who work as baristas (coffee bartenders). All of the employees 
#              have the same hourly pay rate. Megan has asked you to design a 
#              program that will allow her to enter the number of hours worked 
#              by each employee, and then display the amounts of all the 
#              employees' gross pay. You determine the program should perform 
#              the following steps:
#              1. For each employee: get the number of hours worked and store 
#                 it in a list element.
#              2. For each list element: use the value stored in the element 
#                 to calculate an employee's gross pay. Display the amount of 
#                 the gross pay.
# =============================================================================

print("=" * 60)
print("EXERCISE 2: Employees Pay Program")
print("=" * 60)

# Constants
NUM_EMPLOYEES = 6  # Number of employees
HOURLY_PAY_RATE = 15.00  # Hourly pay rate (same for all employees)

# Initialize list to store hours worked
hours_worked = []

# Get hours worked for each employee
# Try-except block: Handles exceptions that may occur during input conversion
try:
    print(f"Enter hours worked for {NUM_EMPLOYEES} employees:")
    print(f"Hourly pay rate: ${HOURLY_PAY_RATE:.2f}")
    
    # Loop (for): Iterates for each employee to collect hours worked
    for employee in range(1, NUM_EMPLOYEES + 1):
        while True:
            # Loop (while True): Continuously prompts until valid hours are provided
            try:
                hours = float(input(f"  Enter hours worked for employee {employee}: "))
                if hours < 0:
                    print("    Error: Hours worked cannot be negative. Please try again.")
                    continue  # Continue loop to ask for input again
                hours_worked.append(hours)  # Add hours to the list
                break  # Exit the while loop when valid input is processed
            except ValueError:
                # Handle invalid numeric input (e.g., non-numeric characters)
                print("    Error: Please enter a valid number.")
    
    # Calculate and display gross pay for each employee
    print("\n" + "=" * 60)
    print("EMPLOYEE GROSS PAY REPORT")
    print("=" * 60)
    print(f"Hourly Pay Rate: ${HOURLY_PAY_RATE:.2f}")
    print(f"\nEmployee\tHours Worked\tGross Pay")
    print("-" * 50)
    
    # Loop (for): Iterates through each employee to calculate and display gross pay
    for i in range(len(hours_worked)):
        gross_pay = hours_worked[i] * HOURLY_PAY_RATE  # Calculate gross pay
        print(f"Employee {i + 1}\t{hours_worked[i]:.2f}\t\t${gross_pay:.2f}")
    
    # Calculate and display totals
    total_hours = sum(hours_worked)  # Calculate total hours worked
    total_gross_pay = total_hours * HOURLY_PAY_RATE  # Calculate total gross pay
    print("-" * 50)
    print(f"Total\t\t{total_hours:.2f}\t\t${total_gross_pay:.2f}")
    
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 3: Exam Grades Program
# =============================================================================
# Description: Dr. LaClaire gives a series of exams during the semester in her 
#              chemistry class. At the end of the semester, she drops each 
#              student's lowest test score before averaging the scores. She has 
#              asked you to design a program that will read a student's test 
#              scores as input and calculate the average with the lowest score 
#              dropped.
# =============================================================================

print("=" * 60)
print("EXERCISE 3: Exam Grades Program")
print("=" * 60)

# Initialize list to store test scores
test_scores = []

# Get test scores from user
# Try-except block: Handles exceptions that may occur during input conversion
try:
    print("Enter test scores (enter -1 to finish):")
    
    # Loop (while True): Continuously prompts until user enters -1 to finish
    while True:
        try:
            score = float(input("  Enter a test score (or -1 to finish): "))
            
            if score == -1:
                # User entered -1 to finish entering scores
                break  # Exit the loop
            elif score < 0 or score > 100:
                # Validate score range
                print("    Error: Test score must be between 0 and 100. Please try again.")
                continue  # Continue loop to ask for input again
            else:
                test_scores.append(score)  # Add score to the list
                print(f"    Score {score} added. Total scores: {len(test_scores)}")
                
        except ValueError:
            # Handle invalid numeric input (e.g., non-numeric characters)
            print("    Error: Please enter a valid number.")
    
    # Process test scores
    if len(test_scores) < 2:
        print("\nError: You must enter at least 2 test scores to calculate average with lowest dropped.")
    else:
        # Display all scores
        print(f"\nAll test scores entered: {test_scores}")
        
        # Find and remove lowest score
        lowest_score = min(test_scores)  # Find the lowest score
        scores_without_lowest = test_scores.copy()  # Create a copy of the list
        scores_without_lowest.remove(lowest_score)  # Remove the lowest score
        
        # Calculate average with lowest score dropped
        average_without_lowest = sum(scores_without_lowest) / len(scores_without_lowest)
        
        # Display results
        print("\n" + "=" * 60)
        print("EXAM GRADES ANALYSIS")
        print("=" * 60)
        print(f"Number of test scores: {len(test_scores)}")
        print(f"All test scores: {test_scores}")
        print(f"Lowest score (dropped): {lowest_score}")
        print(f"Scores used for average: {scores_without_lowest}")
        print(f"Average with lowest score dropped: {average_without_lowest:.2f}")
        
        # Calculate average with all scores for comparison
        average_with_all = sum(test_scores) / len(test_scores)
        print(f"\nAverage with all scores (for comparison): {average_with_all:.2f}")
        
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
print("1. List Operations in Python:")
print("   - min(), max(), sum() functions for list analysis")
print("   - List methods: append(), remove(), copy()")
print("   Source: Python Documentation - Built-in Functions")
print("   https://docs.python.org/3/library/functions.html")
print()
print("2. Payroll Calculation:")
print("   - Gross Pay = Hours Worked × Hourly Rate")
print("   Source: Standard payroll calculation formula")
print()
print("3. Statistical Calculations:")
print("   - Average = Sum of values / Number of values")
print("   - Dropping lowest score before averaging")
print("   Source: Standard statistical methods for grade calculation")
