#Write a Python Program to Check Armstrong Number?

num = int(input("Enter the number : "))
num_len = len(str(num))
temp_num = num
sum_of_digit = 0

while temp_num > 0 :
    digit = temp_num % 10 
    sum_of_digit += digit ** num_len
    temp_num//=10


if num == sum_of_digit:
    print(f"The number {num} is an armstrong number.")
else:
    print(f"The number {num} is not an armstrong number.")
