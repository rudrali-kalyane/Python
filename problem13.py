#Write a Python Program to Check Prime Number.

num = int(input("Enter the number : "))

flag = False

if num == 1 :
    print(f"{num} is not a prime number")

else :
    for i in range (2, int(num*0.5)):
        if num%i == 0:
            flag = True
            break

if flag :
    print(f"{num} is not a prime number ")

else :
    print(f"{num} is a prime number")


#Write a Python Program to Print all Prime Numbers in an Interval of 1 -100.
lower = 1
upper = 100

for num1 in range (lower,upper):
    if num1 > 1 :
        for i in range(2,int(num1*0.5)):
            if num1 % i == 0 :
                break
        else :
            print(num1)


