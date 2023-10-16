#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 15, 2023
# This program will ask the user
# for a number and will tell them
# if they guessed correctly
import constants


def main():
    # Get the user guess
    print("This program will ask the user for a number between 1 and 10")
    print("then it will display if they guessed correctly or not.")
    user_guess = int(input("Please enter your guess between 1 and 10: "))

    # Check if the user guess is equal to correct guess
    if user_guess == constants.CORRECT_GUESS:
        # Display if the user is right
        print("")
        print("Congratulations, that was the correct number")

    # Check if the user guess is not equal to correct guess
    if user_guess != constants.CORRECT_GUESS:
        # Display if the user is wrong
        print("")
        print("Please guess again")


if __name__ == "__main__":
    main()
