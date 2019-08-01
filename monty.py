'''
Monty Hall Problem

Background info:
Based on the famous gameshow where contestants have a choice to pick between 3 doors
Two doors contain goats, and the contestant loses the game
One door contains money, which is what the contestant desires

Rules:
- The contestant picks one closed door at random, not knowing what is behind it
- The host opens one of the other doors, and reveals a goat regardless of what lies behind the contestants' door
- The host gives the contestant a choice, whether to switch doors or not with the other remaining closed door
- The contestant makes their choice and their final choice is revealed

Theory:
In the stage where the host opens a door revealing a goat, it might be thought that there is a 50/50 chance if the contestant wins the money or not
However, this is incorrect. 
Looking at the problem more closley; the contestant makes their first choice by picking one of three doors.
Therefore they have a 1 in 3 chance of getting the correct door in their initial guess.
However, if the contestant refuses to change doors when the host reveals one with a goat, their odds will remain the same.
But, if the contestant chooses to change doors, they now have a 2 in 3 chance of getting the money. 

The purpose of this program is to test the theory as to whether or not it stands after multiple repeated trials


Program made by Eren Sulutas

'''

import random

change_door = True
trials = 10
wins = 0

for i in range(trials):
    # Makes a list of goats 
    door = ["goat"] * 3

    # One door at random will contain money
    door[random.randint(0,2)] = "money"

    selection_index = random.randint(0,2)
    selection = door[selection_index]

    if change_door:
        if selection_index == 0:
            if door[1] == "goat":
                selection = door[2]
            else:
                selection = door[1]
        elif selection_index == 1:
            if door[0] == "goat":
                selection = door[2]
            else:
                selection = door[0]
        else:
            if door[0] == "goat":
                selection = door[1]
            else:
                selection = door[0]

    if selection == "money":
            wins +=1         

print("\nResults:\nCorrect door chosen: {}\nNumber of trials: {}\n".format(wins, trials))