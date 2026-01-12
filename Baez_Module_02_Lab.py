# -------------------------------------------------
# File Name: Baez_Module_02_Lab.py
# Author: Florentino Báez
# Date: Module 02 Lab
# Description: Programming exercises including:
#              1. Distance Traveled Program
#              2. Tip, Tax, and Total Program
#              3. Graphics (4 different shapes)
#              4. BMI Calculator (Extra Credit)
# -------------------------------------------------

import turtle
import math

# =============================================================================
# EXERCISE 1: Distance Traveled Program
# =============================================================================

print("=" * 60)
print("EXERCISE 1: Distance Traveled Program")
print("=" * 60)

# Constants
SPEED = 70  # miles per hour
TIMES = [6, 10, 15]  # hours

# Calculate and display distances
for time in TIMES:
    distance = SPEED * time
    print(f"The distance the car will travel in {time} hours: {distance} miles")

print()

# =============================================================================
# EXERCISE 2: Tip, Tax, and Total Program
# =============================================================================

print("=" * 60)
print("EXERCISE 2: Tip, Tax, and Total Program")
print("=" * 60)

# Constants
TAX_RATE = 0.07  # 7% sales tax
TIP_RATE = 0.18  # 18% tip

# Get user input
try:
    food_charge = float(input("Enter the charge for the food: $"))
    
    # Calculate amounts
    tip_amount = food_charge * TIP_RATE
    tax_amount = food_charge * TAX_RATE
    total = food_charge + tip_amount + tax_amount
    
    # Display results
    print(f"\nFood charge: ${food_charge:.2f}")
    print(f"Tip (18%): ${tip_amount:.2f}")
    print(f"Sales tax (7%): ${tax_amount:.2f}")
    print(f"Total: ${total:.2f}")
    
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 3: Graphics (4 different shapes)
# =============================================================================

print("=" * 60)
print("EXERCISE 3: Graphics")
print("=" * 60)
print("Creating 4 different graphics...")

# Create turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Module 02 Lab - Graphics")

# Create turtle object
t = turtle.Turtle()
t.speed(3)

# Graphic 1: Red Circle (top left)
t.penup()
t.goto(-300, 200)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(50)
t.end_fill()

# Graphic 2: Blue Square (top right)
t.penup()
t.goto(200, 200)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

# Graphic 3: Green Triangle (bottom left)
t.penup()
t.goto(-250, -150)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# Graphic 4: Orange Star (bottom right)
t.penup()
t.goto(200, -100)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for _ in range(5):
    t.forward(80)
    t.right(144)
t.end_fill()

# Hide turtle
t.hideturtle()

print("Graphics created successfully!")
print("Close the graphics window to continue...")
print("(The program will continue after a short delay)")
print()

# Wait a bit, then close (optional - you can close manually)
screen.exitonclick()  # Click to close, or use screen.bye() to auto-close

# =============================================================================
# EXERCISE 4: BMI Calculator (Extra Credit)
# =============================================================================

print("=" * 60)
print("EXERCISE 4: BMI Calculator (Extra Credit)")
print("=" * 60)

try:
    # Get user input
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    
    # Calculate BMI
    # BMI formula: (weight in pounds / (height in inches)^2) * 703
    bmi = (weight / (height ** 2)) * 703
    
    # Classify BMI
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi < 25.0:
        classification = "Normal"
    elif 25.0 <= bmi < 30.0:
        classification = "Overweight"
    else:  # bmi >= 30.0
        classification = "Obese"
    
    # Display results
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Weight Classification: {classification}")
    
    # Display BMI chart reference
    print("\nBMI Classification Chart:")
    print("  Below 18.5     - Underweight")
    print("  18.5 - 24.9    - Normal")
    print("  25.0 - 29.9    - Overweight")
    print("  30.0 or higher - Obese")
    
except ValueError:
    print("Error: Please enter valid numbers for weight and height.")
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
print("1. Distance formula: Distance = Speed * Time (standard physics formula)")
print("2. BMI calculation formula: CDC - Body Mass Index (BMI)")
print("   Source: https://www.cdc.gov/healthyweight/assessing/bmi/index.html")
print("3. Python Turtle Graphics: Python Documentation")
print("   Source: https://docs.python.org/3/library/turtle.html")
