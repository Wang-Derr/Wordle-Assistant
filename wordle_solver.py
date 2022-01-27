import argparse

def incorrectGuessLengthHandler(guess):
    # handler for guesses that are not the correct length
    if (len(guess) == 5 or len(guess) == 0):
        return guess
    else:
        while True:
            new_guess = input("Your guess was not 5 letters please try again...\n")
            if (len(new_guess) == 5 or len(new_guess) == 0):
                break
        return new_guess

def dictCheck(guess):
    # makes sure the first guess is found within the Wordle dictionary
    return guess.lower() in dict_list

def wordPruning():
    # prunes unapplicable words from the dictionary list
    pass

def letterParser():
    # parses through a word to determine where a letter has been placed
    pass

def wordEntryHandler():
    # Process the user supplied info on (in)correct letter(s)
    # ask how many letters were incorrect and which letter(s) then prune all words with these letters
    # ask how many letters were correct but in the wrong place and which letter(s) then prune all words that have the letter in the wrong spot
    # ask how many letters were correct and which letter(s) then prune all words that have different letters in the same spot
    pass

def randomWordGenerator():
    # Generate a random word with the supplied information
    pass

def wordbankGenerator():
    # Generate a wordbank with the supplied information
    pass

def modeHandler(mode):
    if (mode):
        wordbankGenerator()
    else:
        randomWordGenerator()

def subSequentRounds():
    # guess rounds 2 - 6 should be identical in formatting
    pass

# import wordle dictionary into a list
dict_file = open("wordle-dictionary-full.txt", "r")
dict_list = dict_file.read()

# parse user input for mode of operation
parser = argparse.ArgumentParser()
parser.add_argument('--mode', metavar='<random | wordbank>', type=str, required=True)
args = parser.parse_args()
mode_str = args.mode
while (True):
    if (mode_str == 'random'):
        mode = 0
        break
    elif (mode_str == 'wordbank'):
        mode = 1
        break
    else:
        print("\nUnsupported mode: ", mode_str, " submitted\n")
        mode_str = input("please submit either 'random' or 'wordbank' \n")

# round 1
first_guess = input("What would you like your first guess to be? (leave empty for default first guess of 'arose')\n")
first_guess = incorrectGuessLengthHandler(first_guess)
if (len(first_guess) == 5):
    while(not dictCheck(first_guess)):
        first_guess = input("Your word was not found within the Wordle dictionary please enter another or leave blank to use 'arose'\n")
        if (len(first_guess) == 0):
            first_guess = 'arose'
            break
        first_guess = incorrectGuessLengthHandler(first_guess)
else:
    first_guess = 'arose'
first_guess = first_guess.lower()
print("Please try <", first_guess, "> for your first guess")

# round 2

# round 3

# round 4

# round 5

# round 6
