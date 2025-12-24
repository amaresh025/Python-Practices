# Write a program that will check whether the number is an Armstrong number or not.

num_str = input("Enter a number: ")
num = int(num_str)

n = len(num_str)
total = 0

for digit in num_str:
    total += int(digit) ** n

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
