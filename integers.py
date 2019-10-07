#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: October 2019
# This program identifies if an integer is positive, negative or zero


def main():
    # This function tells you if a number is positive, negative, or equal to 0

    # input
    user_input = int(input("Enter an integer: "))

    # process
    if user_input > 0:
        print("This is a positive integer. ")
    elif user_input < 0:
        print("This is a negative integer. ")
    elif user_input == 0:
        print("This integer is zero. ")


if __name__ == "__main__":
    main()
