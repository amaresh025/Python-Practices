# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period in years: "))


simple_interest = (principal * rate * time) / 100

print(f"The simple interest is : {simple_interest:.2f}")
          
