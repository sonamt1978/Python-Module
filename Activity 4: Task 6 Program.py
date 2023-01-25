import random
print("Rolling the dice...")
def roll():
    dice_roll = random.randrange(1, 7)
    print("You rolled a", dice_roll)
print("1. Roll again")
print("2. Exit")
while True:
    roll_again=int(input("Enter your choice:"))
    if roll_again== 1:
        roll()
    else:
        print("Exited the Game")
        break
