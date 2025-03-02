#Write a Python Program to Print the Fibonacci sequence.
nterm = int(input("Enter the number : "))

n1,n2 = 0,1
count = 0

if nterm <= 0 :
    print("Please Enter Positive Number")

elif nterm == 1:
    print(f"Fibonacci series upto {nterm} : {n1}")

else :
    print("Fibonacci Series : ")
    while count < nterm :
        nth = n1+n2
        print(n1)
        n1 = n2
        n2 = nth
        count += 1