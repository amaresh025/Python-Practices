# Write a program that will take three digits from the user and add the square of each digit.

num1 = int(input("Enter first digit : "))
num2 = int(input("Enter second digit : "))
num3 = int(input("Enter third digit : "))

square_sum = num1 ** 2 + num2 ** 2 + num3 ** 2

print(f"Add squre of three digit {num1}, {num2}, {num3} is : {square_sum}")