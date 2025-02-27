#Write a Python program to do arithmetical operations addition and division.

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

add = num1+num2
print(f"Addition of number {num1} and {num2} is {add}")

if num2==1:
    print("Division is not possible")

else:
    print(f"Division of {num1} by {num2} is {num1/num2}" )