#Write a Python Program to Find the Factorial of a Number.

num = int(input("Enter the number : "))

fact = 1 

if num < 0 :
    print("Factorial does not exist for negative number")

elif num == 0 :
    print(f"factorial for {num} is 1")

else:
    for i in range(1,num+1) :
        fact *=i

    print(f"Factorial of {num} is {fact}")