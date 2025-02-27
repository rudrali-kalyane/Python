#Write a Python program to swap two variables.

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
print(f"Values of numbers before swapping num1 = {num1}, num2 = {num2}")

#with temp variable

temp = num1
num1 = num2
num2 = temp 

print(f"Values of numbers after swapping num1 = {num1}, num2 = {num2}")

print(f"\n\nValues of numbers before swapping num1 = {num1}, num2 = {num2}")

num1 = num1 + num2 
num2 = num1 - num2
num1 = num1 - num2
print(f"Values of numbers after swapping num1 = {num1}, num2 = {num2}")
