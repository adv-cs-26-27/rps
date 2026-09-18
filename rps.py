import random   # imports a library (named random) for making random choices

def get_user_name():
    """
    gets the user's name and prints a welcome message
    arguments:  none
    returns:    nothing
    """
    user_name = input("What is your name? ")
    print("Welcome,", user_name, "!")
    print("Ready for RPS? Choose wisely!!")

def get_user_choice():
    """
    gets the user's choice and returns it
    arguments:  none
    returns:    the user's choice, a string
    """
    user_choice = "" # TODO: get user input and validate it
    return user_choice

def get_comp_choice():
    """
    uses the random library to get the computer's choice
    arguments:  none
    returns:    the computer's choice, a string
    """
    comp_choice = random.choice(["rock", "paper", "scissors"])
    return comp_choice

def rps(user, comp):
    """
    runs a game of rock-paper-scissors
    arguments:  user and comp, both strings 
                (either 'rock' 'paper' or 'scissors')
    returns: nothing
    """
    # print both choices
    print("You chose", user)
    print("I chose", comp)

    # TODO: implement the logic of the game!

# calling the get_user_name() function
get_user_name()

# getting both the user and comp choices by calling 
# the respective functions and storing them in variables
user_choice = get_user_choice()
comp_choice = get_comp_choice()

# call the rps() function, passing the user_choice 
# and comp_choice variables as arguments
rps(user_choice, comp_choice)

def test_rps():
    pass
    # TODO: confirm that your game works properly
    # for all cases