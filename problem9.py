#Write a Python program to solve quadratic equation.

import math

a = float(input("Enter the coefficeint of a : "))
b = float(input("Enter the coefficeint of b : "))
c = float(input("Enter the coefficeint of c : "))

discriminant = b**2 - 4*a*c

if discriminant > 0 :
    root1 = (- b + math.sqrt(discriminant))/2*a
    root2 = (- b - math.sqrt(discriminant))/2*a

    print(f"root1 : {root1}")
    print(f"root2 : {root2}")

elif discriminant == 0 :
    root = - b/2*a
    print(f"root : {root}")

else :
    real_part = -b/2*a
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)

    print(f"root1 : {real_part} + {imaginary_part}i")
    print(f"root2 : {real_part} - {imaginary_part}i")
    