# User will input (3ages).Find the oldest one

"""
age1 = int(input("age1 is : "))
age2 = int(input("age2 is : "))
age3 = int(input("age3 is : "))

oldest = max(age1, age2, age3)

print("the oldest is : ", oldest)

"""


def max_age(age_one, age_two, age_three):
    old = max(age_one, age_two, age_three)
    return old

print(max_age(41, 52, 21))
