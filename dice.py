## Important things to remember. I was adding the module wrong. Project>AddNewItem>AddEmptyModule ##
## This is how you use more than one script for a project as well as how to communicate between the two ##
########################################### VERY IMPORTANT ############################################### 
import random
from dataclasses import dataclass

@dataclass
class Die:
    value:int = 1 # If you want this to be private add double underscore to the prefix.

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
