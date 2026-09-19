"""
School Circular Garden Detail Calculator
-Purpose - Determines the area rounded down and up, the circumference, and the square root of the area to 2 decimal places, based on a radius input by the user.
-Author - Luoang
-Sept. 19, 2026
"""

import math

#-Input stage-
#gets the radius from user for determining details
radius = float(input("Please enter the radius of the school garden in meters. \n")) #\n inserts a new line for easier readability, float() is used to convert input result (string) to float

#-Processing stage-
pi = math.pi #defining pi from the math library for exact computation rather than manually entering 3.14159...

area = pi * math.pow(radius, 2) #pi times the radius squared using math.pow() - area formula
circ = 2 * pi * radius #2 times pi times r - circumference formula
area_sqrt = math.sqrt(area) #finds the square root of the area using math.sqrt()

area_roundup = math.ceil(area)
area_rounddown = math.floor(area)

#-Output stage-
#:.2f displays the variables to 2 decimal places; f-strings are used for easier variable injection
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circ:.2f} meters")
print(f"Square root of the area: {area_sqrt:.2f}")
print(f"Area rounded down: {area_rounddown} square meters")
print(f"Area rounded up: {area_roundup} square meters")