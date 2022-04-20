#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: April 20 2022
# Find the factorial of a number


def main():
    counter = 0
    factorial_num = 1
    # Get inputs
    user_num_str = input("What number do you want to find the factorial of: ")
    # try catch
    try:
        user_num = int(user_num_str)
    except:
        print("You have to input integers greater that 0")
        main()
    # check if below 0
    if user_num < 0:
        print("You have to input integers greater than 0")
        main()
    while counter < user_num:
        counter += 1
        print("Tracking {} times".format(counter))
        factorial_num = counter * factorial_num
        if counter >= user_num:
            break
    print("The answer facotialed is {}".format(factorial_num))


if __name__ == "__main__":
    main()
