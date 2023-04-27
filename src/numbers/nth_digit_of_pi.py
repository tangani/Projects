"""
Name: nth_digit_of Pi
Purpose: Get the value of Pi to the n number of decimal places
Author: Molisa (Tangani)
Algorithm: 
Licence: MIT


"""

import math

while True:
    nth_number = int(input("What nth decimal number of pi do you want? \t"))

    print(math.pi)

    start = 0
    current = 22
    pi_list = []
    while start <= nth_number:
        pi_list.append(current/7)

        start += 1

    print(pi_list)

    break