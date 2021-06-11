#Python:    3.9.4
#
#Author:    Neil Javier
#
#Purpose:   Exercise Python logic through building a multiple choice game.


def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
   




def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player for
        playing again and continue with the game
    """

    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get thier name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    # create variable based on user input that declares how many attempts they want to make win.
                    # the global keyword tells the program that the variable inside this function will be global instread of local
                    global attempts
                    attempts = int(input("\nHow many attempts would you like to make, {}?: ".format(name)))
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a \nconversation. WIll you be nice \nor mean? (N/M) \n>>>: ').lower()
        if pick == "n":
            print("\nThe stranger walks away smiling..")
            nice = (nice +1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
        score(nice,mean,name) #pass the 3 variables to the score

def show_score(nice,mean,name):
    print("\n{}, your current score total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))



def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variable
    if nice > attempts: #if condition is valid, call win function passing in the variable so it can use them
                 #originally set to '2', i customized to let the user determine the number of attempts
        win(nice,mean,name)
    if mean > attempts: #if condition is valid, call lose function passing in the variable so it can use them
        lose(nice,mean,name)
    else:       #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    # substitute the {} wildcards with our varible values
    print('\nNice job{}, you win! \nEveryone loves you and youve \nmade lots of friends along the way!'.format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #Substitute the {} wildcards with out variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in our variable
    again(nice,mean,name)
    

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('Do you want to play again? (y/n):\n... ').lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\Enter ( Y ) for 'Yes', and ( N ) for 'No':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as the same user has electted to play again
    start(nice,mean,name)
        


if __name__ == "__main__":
    start()

                  
