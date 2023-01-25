import random
random_number = random.randint(1, 20)
while True:
    user_guess = int(input("Guess number between 1 and 20: "))
    if user_guess == random_number:
        print("You guessed the correct number.")
        break
    elif user_guess < random_number:
        print("Your guess is too low. Please try again.")
    else:
        print("Your guess is too high. Please try again.")
