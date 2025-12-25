# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).

salary = float(input("Enter basic salary : "))

hra = salary * 0.10
da = salary * 0.05
pf = salary * 0.03
 
tax = 0
if salary <= 100000:
    print("k")
    exit()
elif salary < 500000:
    tax = 0
elif salary < 1100000:
    tax = salary * 0.10
elif salary <= 2000000:
    tax = salary * 0.20
else :
    tax = salary * 0.30


total_deduction = hra + da + pf + tax

in_hand = salary - total_deduction

print(f"Basic Salary     : ₹{salary:.2f}")
print(f"Total Deduction : ₹{total_deduction:.2f}")
print(f"In-hand Salary   : ₹{in_hand:.2f}")
