#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Apr 2022
# This program checks if someone can vote in Canada


def main():
    # This function checks age for voting

    # input
    string = input("Please enter your age: ")

    # process & output
    print("")
    try:
        age = int(string)
        if age < 0:
            print("That is not possible, or very very confusing.")
        elif age >= 18:
            print("You can vote in Canada!")
        else:
            print("You can not vote in Canada.")
    except Exception:
        print("{} is not an age.".format(string))

    print("\nDone.")


if __name__ == "__main__":
    main()
