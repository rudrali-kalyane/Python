#Write a Python Program to Display the multiplication Table.

num = int (input("Enter the number : "))
print(f"Multiplication table of {num} : ")
for i in range (1,11):
    print(f"{num} x {i} = {num*i}")