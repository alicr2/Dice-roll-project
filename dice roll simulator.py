import random


def roll_dice():
    print("Rolling the dice...")
    return random.randint(1, 6)


print("Welcome to my dice rolling simulator")
while True:
    input("press enter to roll the dice,or type quit to exit...")
    dice_result = roll_dice()
    
    print("You rolled a", dice_result)