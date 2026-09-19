# Circular Garden Detail Calculator

## Purpose/Problem
This program displays the area (in 3 different ways), circumference, and square root of the area of a circular garden the school plans to build.

### Steps
- Get radius (as a float) from user
- Calculate the area using pi * radius squared (as a float)
- Calculate the circumference using 2 * pi * radius (as a float)
- Determine the floor and ceiling (both integers) of the area using the floor and ceiling functions in math
- Print each calculated result to 2 decimal places if applicable


## Pseudocode algorithm
radius = input "Enter radius: "

area = pi * radius ^ 2
circ = 2 * pi * radius
sqrt_area = sqrt(area)
area_roundup = ceiling(area)
area_rounddown = floor(area)

display "Area: {area:.2f}"
display "Circumference: {circ:.2f}"
display "Square root of area: {sqrt_area:.2f}"
display "Ceiling of area: {area_roundup:.2f}"
display "Floor of area: {area_rounddown:.2f}"
