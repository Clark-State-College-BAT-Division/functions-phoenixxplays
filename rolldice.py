#Write a function that takes as input number of dice and number of sides. The function will then return a list
#of randomly generated numbers in the proper count and range. For example if the the function is asked to generate
#3D6 or three sixed sided dice, then a potential output would be [2,2,6]
#This function cannot have any input or print statements.
#Write supporting code that will as the user for number of dice and sides, call the function, then report the results.
#The function should not be called if number of dice is zero or less and instead should report bad input to the user
#The function should not be called if number of sides is 1 or less and instead should report bad input to the user
#Sample outputs (your text does not have to match exactly)

# How many dice to roll? 3
# How many sides? 6
# Here are the results: [6, 1, 6]

# How many dice to roll? 0
# How many sides? 5
# Error: Sides must be greater than 1 and dice count greater than 0.

# How many dice to roll? 20
# How many sides? 20
# Here are the results: [18, 19, 6, 8, 13, 6, 6, 6, 18, 12, 20, 10, 14, 8, 14, 17, 12, 15, 20, 17]
import sys

import random

random.seed()

#function is writing how the dice will be randomized
#results = random number generated between 2 and diceSides, diceCount many times
def RandomDice(diceCount, diceSides):
    diceList = []
    for i in range(diceCount):
        result = random.randint(2,diceSides)
        diceList.append(result)
        return result
    return diceList
    
# loopCount = 0

diceCount = int(input("How many dice to roll: "))

diceSides = int(input("How many sides?: "))
    
if diceCount <= 0:
    print("Error: You must roll at least 1 dice.")
    sys.exit(1)
if diceSides <= 1:
    print("Error: The number of sides must at least be 2 sides.")
    sys.exit(2)


for i in range(diceCount):
    # while loopCount < diceCount:
    # RandomDice(diceCount, diceSides)
        result = RandomDice(diceCount, diceSides)

print(f"Here are the results: {result}")