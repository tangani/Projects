#!/usr/bin/env python

"""
Name: Calculator.py
Purporse: A simple calculator to do basic operators. Make it a scientific
    calculator for added complexity.
Author: Molisa (tangani)
Algorithm:
Licence: MIT

"""

def calc(first, second, operator):

    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        return first / second


def main():
    a = int(input("Please enter the first number: \t"))
    b = int(input("Please enter the first number: \t"))
    op = input("Choose an operatoe between: \
                     \n \t*, -, +, /: \t")

    print(f"{a} {op} {b} = {calc(a, b, op)}")


if __name__ == '__main__':
    main()
