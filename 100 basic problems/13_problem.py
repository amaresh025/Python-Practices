# Write  a program that will tell whether the given number is divisible by 3 & 6.

num = int(input("Enter a number : "))
if num == 0:
    print("0 is divisible by every non-zero integer")

elif num % 6 == 0:
    print(f"{num} is divisible by 3 and 6")

elif num % 3 == 0:
   print(f"{num} is divisible by 3 but not by 6")

else:
    print(f"{num} is not divisible by 3 and 6")