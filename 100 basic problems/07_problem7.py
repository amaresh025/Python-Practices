# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter a Year : "))

if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")