#Write a Python Program to Find Armstrong Number in an Interval.
lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))

for num in range (lower, upper+1) :

    num_len = len(str(num))
    temp_num = num
    sum_of_digit = 0

    while(temp_num > 0) :
        digit = temp_num % 10
        sum_of_digit += digit ** num_len
        temp_num //=10

    if num == sum_of_digit :
        print(num)