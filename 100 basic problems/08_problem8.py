# Write a program to find the euclidean distance between two coordinat
import math

x1 = float(input("enter x1 : "))
x2 = float(input("enter x2 : "))
y1 = float(input("enter y1 : "))
y2 = float(input("enter y2 : "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The euclidean distance between {x1, x2} and {y1, y2} = {distance:.2f}")