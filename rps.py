import random       # imports a library (named random) for making random choices

user_name = input("What is your name? ")
print("Welcome,", user_name, "!")
print()

print("Ready for RPS? Choose wisely!!")
comp_choice = random.choice(["rock", "paper", "scissors"])
user_choice = "" # TODO: get user input

# print both choices
print("You chose", user_choice)
print("I chose", comp_choice)
print()

# TODO: implement the logic of the game!
