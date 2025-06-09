## Important things to remember. I was adding the module wrong. Project>AddNewItem>AddEmptyModule ##
## This is how you use more than one script for a project as well as how to communicate between the two ##
########################################### VERY IMPORTANT ############################################### 
import random
from dataclasses import dataclass

@dataclass
class Die:
    __value:int = 1 # If you want this to be private add double underscore to the prefix.

    # If the value is between 1 and 6 continue. If not closes the program.
    def getValue(self):
        return self.__value
    def setValue(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        else:
            self.__value = value

    def roll(self):
        self.value = random.randrange(1, 7)

# Object composition is a way to combine simple objects into more complex ones.
# e.x. one Dice object can store multiple Die objects.
class Dice():
    # Explicit constructor
    def __init__(self):
        self.list = []

    def addDie(self, die):
        self.list.append(die)

    def rollAll(self):
        for die in self.list:
            die.roll()
