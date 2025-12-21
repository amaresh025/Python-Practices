# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num = input("Four digit No. is : ")

reverse = int(str(num)[::-1])
print("Reverse of {num} is : ", reverse)

