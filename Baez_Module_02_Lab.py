# -------------------------------------------------
# File Name: Baez_Module_02_Lab.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
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
# Description: Assuming there are no accidents or delays, the distance that a 
#              car travels down the interstate can be calculated with the 
#              following formula:
#
#              Distance = Speed * Time
#
#              A car is traveling at 70 miles per hour. Write a program that 
#              displays the following:
#              • The distance the car will travel in 6 hours
#              • The distance the car will travel in 10 hours
#              • The distance the car will travel in 15 hours
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
# Description: Write a program that calculates the total amount of a meal 
#              purchased at a restaurant. The program should ask the user to 
#              enter the charge for the food, then calculate and display the 
#              amount of an 18 percent tip, the amount of a 7 percent sales 
#              tax, and the total of all three amounts.
# =============================================================================

print("=" * 60)
print("EXERCISE 2: Tip, Tax, and Total Program")
print("=" * 60)

# Constants
TAX_RATE = 0.07  # 7% sales tax
TIP_RATE = 0.18  # 18% tip

# Get user input with exception handling for invalid input
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
    # Handle invalid numeric input
    print("Error: Please enter a valid number.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"Error: {e}")

print()

# =============================================================================
# EXERCISE 3: Graphics (4 different shapes)
# =============================================================================
# Description: Write a program that uses the turtle graphics library to draw 
#              four different shapes on the screen. The program should display:
#              • A red circle (top left)
#              • A blue square (top right)
#              • A green triangle (bottom left)
#              • An orange star (bottom right)
# =============================================================================

print("=" * 60)
print("EXERCISE 3: Graphics")
print("=" * 60)
print("Creating 4 different graphics...")

# Create turtle screen
screen = turtle.Screen #create a turtle screen object
screen.setup(width=800, height=600) #set the width and height of the screen
screen.bgcolor("white") #set the background color to white
screen.title("Module 02 Lab - Graphics") #set the title of the screen

# Create turtle object
t = turtle.Turtle() #create a turtle object
t.speed(3) #set the speed of the turtle to 3

# Graphic 1: Red Circle (top left)
t.penup() #lift the pen to move the turtle
t.goto(-300, 200) #move the turtle to the top left position
t.pendown() #lower the pen to start drawing
t.fillcolor("red") #set the fill color to red
t.begin_fill() #start filling the shape
t.circle(50) #draw a circle with a radius of 50
t.end_fill() #end filling the shape

# Graphic 2: Blue Square (top right)
t.penup() #lift the pen to move the turtle
t.goto(200, 200) #move the turtle to the top right position
t.pendown() #lower the pen to start drawing
t.fillcolor("blue") #set the fill color to blue
t.begin_fill() #start filling the shape
for _ in range(4): #draw a square with a side length of 100
    t.forward(100) #move the turtle forward by 100 units
    t.right(90) #turn the turtle right by 90 degrees
t.end_fill() #end filling the shape

# Graphic 3: Green Triangle (bottom left)
t.penup() #lift the pen to move the turtle
t.goto(-250, -150) #move the turtle to the bottom left position
t.pendown() #lower the pen to start drawing
t.fillcolor("green") #set the fill color to green
t.begin_fill() #start filling the shape
for _ in range(3): #draw a triangle with a side length of 100
    t.forward(100) #move the turtle forward by 100 units
    t.left(120) #turn the turtle left by 120 degrees
t.end_fill() #end filling the shape

# Graphic 4: Orange Star (bottom right)
t.penup() #lift the pen to move the turtle
t.goto(200, -100)
t.pendown() #lower the pen to start drawing
t.fillcolor("orange") #set the fill color to orange
t.begin_fill() #start filling the shape
for _ in range(5): #draw a star with 5 points
    t.forward(80) #move the turtle forward by 80 units
    t.right(144) #turn the turtle right by 144 degrees
t.end_fill() #end filling the shape

# Hide turtle
t.hideturtle()

print("Graphics created successfully!")
print("Close the graphics window to continue...")
print("(The program will continue after a short delay)")
print()

# Wait a bit, then close.
screen.exitonclick()  # Click to close, or use screen.bye() to auto-close

# =============================================================================
# EXERCISE 4: BMI Calculator (Extra Credit)
# =============================================================================
# Description: Write a program that calculates a person's Body Mass Index (BMI).
#              The program should ask the user to enter their weight in pounds 
#              and height in inches, then calculate and display their BMI. The 
#              program should also classify the BMI as Underweight, Normal, 
#              Overweight, or Obese based on standard BMI ranges.
# =============================================================================

print("=" * 60)
print("EXERCISE 4: BMI Calculator (Extra Credit)")
print("=" * 60)

# Get user input with exception handling for invalid input
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
    
    # Display results with BMI classification
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Weight Classification: {classification}")
    
    # BMI classification chart
    print("\nBMI Classification Chart:")
    print("  Below 18.5     - Underweight")
    print("  18.5 - 24.9    - Normal")
    print("  25.0 - 29.9    - Overweight")
    print("  30.0 or higher - Obese")
    
except ValueError:
    # Handle invalid numeric input
    print("Error: Please enter valid numbers for weight and height.")
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
print("1. Distance formula: Distance = Speed * Time (standard physics formula)")
print("2. BMI calculation formula: CDC - Body Mass Index (BMI)")
print("   Source: https://www.cdc.gov/healthyweight/assessing/bmi/index.html")
print("3. Python Turtle Graphics: Python Documentation")
print("   Source: https://docs.python.org/3/library/turtle.html")
