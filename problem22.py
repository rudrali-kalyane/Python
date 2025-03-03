#Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

while True :

    print("1 -> Addition")
    print("2 -> Subtraction")
    print("3 -> Multiplication")
    print("4 -> Division")
    choice = int(input("Enter Choice (1, 2, 3, 4)"))
    try:
        num1 = float(input("Enter the number : "))
        num2 = float(input("Enter the number : "))
    except ValueError:
        print("Invalid Input.")
        continue

    if choice in (1, 2, 3,4):

        if choice == 1:
            print(f"Addition of {num1} and {num2} is {add(num1,num2)}")

        elif choice == 2:
            print(f"Subtraction of {num1} and {num2} is {sub(num1,num2)}")

        elif choice == 3:
            print(f"Multiplication of {num1} and {num2} is {mult(num1,num2)}")

        elif choice == 4:
            print(f"Division of {num1} by {num2} is {div(num1,num2)}")

        ch = input("Do you want to continue ? (y/n)")
        if ch == 'n' or ch == 'N':
            break

    else:
        print("Invalid Input")
    



    
