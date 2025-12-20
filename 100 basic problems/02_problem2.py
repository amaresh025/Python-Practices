# Write a program that will convert celsius value to fahrenheit
""""

F = (C * 9/5) + 32
C = (F - 32) * 5/9

"""
""""
c = 20.2





f = (c * 9/5) + 32

print("Celcius to Fahrenheit : ", f)

"""

def celcius_to_f(c):
    f = (c * 9/5) + 32
    return f

print(celcius_to_f(float(54)))