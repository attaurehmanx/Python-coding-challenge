import random

def dice_roll():

    range1 = random.randint(1, 6)
    range2 = random.randint(1, 6)

    player1 = range1
    player2 = range2
    print(f"player1 rolled dice: {player1}")
    print(f"player2 rolled dice: {player2}")

dice_roll()