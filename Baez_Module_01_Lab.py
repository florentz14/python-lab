# -------------------------------------------------
# File Name: Baez_Module_01_Lab.py
# Author: Florentino Báez
# Date: Module 01 Lab
# Description: Programming exercises including:
#              1. Simple 3-Column Number Table
#              2. Adding Spacing for Alignment
#              3. 3-Column Fruit Table
#              4. Table with Headings
#              5. Printing a Table with the 'end' Parameter
#              6. Formatting Float Numbers with Precision
#              7. Drawing Shapes with Turtle
# -------------------------------------------------

# Exercise 1: Simple 3-Column Number Table
# In this exercise, we create variables for numbers 1-9 and print them
# in a 3-column table format using basic print statements.

# Create variables for numbers 1 to 9
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9

# Print them in a table (3 per row)
print("Exercise 1: Simple 3-Column Number Table")
print("-" * 20)
print(num1, num2, num3)
print(num4, num5, num6)
print(num7, num8, num9)

# Exercise 2: Adding Spacing for Alignment
# Use f-strings with left-alignment formatting (:<) to create neatly
# aligned columns with consistent spacing.

# Create variables for numbers 1 to 9
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9

# Same numbers but aligned neatly with spaces using f-strings
print("Exercise 2: Adding Spacing for Alignment")
print("-" * 20)
print(f"{num1:<5}{num2:<5}{num3:<5}")
print(f"{num4:<5}{num5:<5}{num6:<5}")
print(f"{num7:<5}{num8:<5}{num9:<5}")

# Exercise 3: 3-Column Fruit Table
# Create a table of fruit names organized in 3 columns using
# f-string formatting with appropriate column widths.

# Variables for fruits
fruit1 = "Apple"
fruit2 = "Banana"
fruit3 = "Cherry"
fruit4 = "Date"
fruit5 = "Fig"
fruit6 = "Grape"
fruit7 = "Kiwi"
fruit8 = "Lemon"
fruit9 = "Mango"

# Print fruits in columns
print("Exercise 3: 3-Column Fruit Table")
print("-" * 40)
print(f"{fruit1:<12}{fruit2:<12}{fruit3:<12}")
print(f"{fruit4:<12}{fruit5:<12}{fruit6:<12}")
print(f"{fruit7:<12}{fruit8:<12}{fruit9:<12}")

# Exercise 4: Table with Headings
print("Exercise 4: Table with Headings")
print("-" * 40)

# Print headings
print(f"{'Item':<12}{'Price':<8}{'Quantity':<8}")
print("-" * 28)

# Row 1
item1 = "Pencil"
price1 = 0.50
qty1 = 20
print(f"{item1:<12}${price1:<7.2f}{qty1:<8}")

# Row 2
item2 = "Notebook"
price2 = 1.75
qty2 = 5
print(f"{item2:<12}${price2:<7.2f}{qty2:<8}")

# Row 3
item3 = "Eraser"
price3 = 0.25
qty3 = 50
print(f"{item3:<12}${price3:<7.2f}{qty3:<8}")


# Exercise 5: Printing a Table with the 'end' Parameter
# Use the end parameter in print statements to control line breaks
# and print table elements on the same line.

print("Exercise 5: Printing a Table with end parameter")
print("-" * 40)

# Printing on the same line using end=""
print("1", end=" ")
print("2", end=" ")
print("3")
print("4", end=" ")
print("5", end=" ")
print("6")
print("7", end=" ")
print("8", end=" ")
print("9")


# Exercise 6: Formatting Float Numbers with Precision
# Format floating-point numbers to 2 decimal places using
# the :.2f format specifier in f-strings.

print("Exercise 6: Formatting Float Numbers with Precision")
print("-" * 40)

# Variables for products with imprecise floating-point values
item1 = "Milk"
price1 = 2.45678  # Has many decimal places
item2 = "Bread"
price2 = 1.2  # Missing decimal places
item3 = "Cheese"
price3 = 4.789  # Has 3 decimal places

# Print table with price formatted to 2 decimal places
print(f"{'Item':<10}{'Price':<10}")
print("-" * 20)
print(f"{item1:<10}{price1:.2f}")
print(f"{item2:<10}{price2:.2f}")
print(f"{item3:<10}{price3:.2f}")


# Exercise 7: Drawing Shapes with Turtle
# Use the turtle module to draw basic shapes (circle, triangle, square)
# with different colors and positions on the screen.

import turtle

# Create a turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set drawing speed

# Draw a red circle
pen.color("red")
pen.begin_fill()
pen.circle(50)  # radius 50
pen.end_fill()

# Move to a new position for the triangle
pen.penup()
pen.goto(-150, -100)
pen.pendown()

# Draw a blue triangle
pen.color("blue")
pen.begin_fill()
for _ in range(3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()

# Move to another position for the square
pen.penup()
pen.goto(100, -100)
pen.pendown()

# Draw a green square
pen.color("green")
pen.begin_fill()
for _ in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# Finish and display the drawing
print("Drawing complete! Close the turtle window to continue.")
turtle.done()
