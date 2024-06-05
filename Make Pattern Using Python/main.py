# QUESTION:

# Write a python script that make a triangle like pattern with the help of turtle library.



# SOLUTION:

# Import every thing from turtle library.
from turtle import *

# List of colors.
c = ["magenta", "blue", "green"]

# For loop for execute below repeatedly until program will done.
for i in range(500):
  # Take color of line from the list of color.
  color(c[i%3])
  # Forward line with the length of (i * 4).
  forward(i * 4)
  # Change direction of line.
  right(121)

# Program is done.
done()