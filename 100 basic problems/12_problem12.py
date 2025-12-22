# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
import math
radius = float(input("Enter radius of cylinder (in cm) :"))
height = float(input("Enter height of cylinder (in cm) :"))

volume_cm3 = math.pi * radius ** 2 *height

liters = volume_cm3 / 1000

cost = liters * 40

print(f"The volume of cylinder is : {liters:.2f} liters")
print(f"The total cost of milk is : ₹{cost:.2f}")
