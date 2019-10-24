#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program can find the factorial of a number using a while loop


def main():
    # This function can find the factorial of a number using a while loop

    # Variables
    factorial = 1
    counter = 0

    # Input
    positive_integer = int(input("Enter a positive integer here: "))
    print("")

    # Process
    while positive_integer > counter:
        counter += 1
        factorial = factorial*counter

    # Output
    print("The factorial of", positive_integer, "is", factorial)


if __name__ == "__main__":
    main()
