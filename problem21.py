#Write a Python Program to calculate the natural logarithm of any number
import math
num = int(input("Enter the number : "))

if num <= 0:
    print("Please enter positive number.")
else :

    print(f"Logarithm of {num} is {math.log(num)}")