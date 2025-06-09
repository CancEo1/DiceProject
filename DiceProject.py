# Purpose: to use classes to hold Die and Dice classes for a Dice program
# This program is how you communicate between two scripts for one program.
# Random and dataclass modules. A single value attribute with a default of 1
# set to public so that calling code can set it to another value.
# roll method set value to random value from 1 to 6
# addDie method to add a Die object with append() method
# rollAll() method to roll all of the Die objects. Looping through each die object
from dice import Dice, Die

def main():
    print("The Dice program")
    print()

    # Get the number of dice from user
    count = int(input("Please enter the number of dice to roll: "))
    print()

    # creat Dice object and add Die objects to it
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    choice = "y"
    while choice.lower() == "y":
        # roll the dice
        dice.rollAll()

        # display to the user
        print("Your Roll: ", end="")
        for die in dice.list:
            print(die.value, end=" ")
        print("\n")
        choice = input("Roll again? (y/n): ")
    print("Goodbye!")

if __name__ == "__main__":
    main()
