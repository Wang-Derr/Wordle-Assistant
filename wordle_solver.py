import argparse
import random
import sys

def incorrectGuessLengthHandler(guess):
    # handler for guesses that are not the correct length
    if (len(guess) == 5 or len(guess) == 0):
        return guess
    else:
        while True:
            new_guess = input("\nYour guess was not 5 letters please try again...\n")
            if (len(new_guess) == 5 or len(new_guess) == 0):
                break
        return new_guess

def incorrectIndexHandler(indices):
    # make sure that user provided index are actual numbers and within the range of 1-5
    new_indices = indices
    while True:
        try:
            all_clear = 0
            while True:
                for x in new_indices:
                    if ((int(x)-1) > 4 or (int(x)-1) < 0):
                        print
                        all_clear = 1
                if (not all_clear):
                    break
                else:
                    new_indices = input("\nThe index of your letter should be in the range of 1-5, please try again...\n")
                    all_clear = 0
            break
        except ValueError:
            new_indices = input("\nYour input includes non-integer values, please try again...\n")
    return new_indices

def repeatIndexHandler(prev_indices, curr_indices):
    # handles repeat user submissions of the same index between incorrect (gray), misplaced (yellow), and correct (green)
    new_indices = curr_indices
    all_clear = 0
    while True:
        for x in prev_indices:
            if new_indices.count(x) > 0:
                all_clear = 1
                print(x, "has already been submitted earlier...")
        if (not all_clear):
            break
        else:
            new_indices = input("\nYou've submitted an index that contradicts with a previous submission, please try again...\n")
            all_clear = 0
    return new_indices

def letterStatusHandler(indices, mode, guess):
    # handles word pruning from the dictionary list
    if (len(indices) == 0):
        return
    else:
        if (mode == 0):
            for x in indices:
                x_index = int(x) - 1
                # remove all words that have incorrect letters
                for y in reversed(dict_list):
                    if (guess[x_index] in y):
                        dict_list.remove(y)
        elif (mode == 1):
            for x in indices:
                x_index = int(x) - 1
                # remove all words with the misplaced letters in the wrong position
                for y in reversed(dict_list):
                    if (guess[x_index] not in y):
                        dict_list.remove(y)
                    if (y[x_index] == guess[x_index]):
                        dict_list.remove(y)
        elif (mode == 2):
            for x in indices:
                x_index = int(x) - 1
                # remove all words with other letters at given index
                for y in reversed(dict_list):
                    if (y[x_index] != guess[x_index]):
                        dict_list.remove(y)

def wordEntryHandler(guess):
    remaining_indices = ['1','2','3','4','5']

    # Process the user supplied info on (in)correct letter(s)
    # ask how many letters were correct and which letter(s) then prune all words that have different letters in the same spot
    correct_indices = input ("\nPlease enter the index of correct (green) letters with no spaces or punctuation between or leave blank if none\n"
                             "(enter as many time as there are instances e.g. '13' for 'ff' in 'fifth')\n")
    correct_indices = incorrectIndexHandler(correct_indices)
    indices_length = len(correct_indices)
    letterStatusHandler(correct_indices, 2, guess)
    if (indices_length >= 5):
        return

    # ask how many letters were correct but in the wrong place and which letter(s) then prune all words that have the letter in the wrong spot
    misplaced_indices = input("\nPlease enter the index of misplaced (yellow) letters with no spaces or punctuation between or leave blank if none\n"
                              "(enter as many time as there are instances e.g. '45' for the 'ff' in 'scoff')\n"
                              "(if you submit a word with two of the same letter but one is green and one is gray, treat the gray one as yellow)\n"
                              "(note that in the case of double letters like 'shook', the 1st 'o' may show up as yellow while the 2nd shows up as gray, please treat them both as yellow)\n")
    misplaced_indices = incorrectIndexHandler(misplaced_indices)
    misplaced_indices = repeatIndexHandler(correct_indices, misplaced_indices)
    indices_length += len(misplaced_indices)
    letterStatusHandler(misplaced_indices, 1, guess)
    if (indices_length >= 5):
        return

    # filter out already submitted indices
    for x in correct_indices+misplaced_indices:
        remaining_indices.remove(x)

    # deduce incorrect letter(s) then prune all words with these letters
    incorrect_indices = ''.join(remaining_indices)
    letterStatusHandler(incorrect_indices, 0, guess)


def subsequentRounds(guess):
    wordEntryHandler(guess)
    # generate weights for words and sort the list with the weights
    weight_list = []
    subweight_list = [0] * 5
    for x in dict_list:
        i = 0
        for y in x:
            if x.count(y) == 0:
                print("The impossible has occured...")
                sys.exit()
            elif x.count(y) == 1:
                subweight_list[i] = 5
                i += 1
            elif x.count(y) == 2:
                subweight_list[i] = 3
                i += 1
            elif x.count(y) == 3:
                subweight_list[i] = 1
                i += 1
            else:
                print("The impossible has occured...")
                sys.exit()
        weight_list.append(min(subweight_list))
    weighted_dict = dict(zip(dict_list, weight_list))
    sorted_dict = list(reversed(sorted(weighted_dict, key=weighted_dict.get)))
    if (mode):
        # Generate a wordbank that a user can select from manually or randomly
        print("\nThis is your current wordbank:\n", sorted_dict)
        wordbank_guess = input("\nPlease choose a word from the wordbank for your next guess or leave blank for a random word from the wordbank\n")
        if (len(wordbank_guess) == 0):
            wordbank_guess = ''.join(random.choices(dict_list, weights=weight_list, k=1))
            return wordbank_guess
        wordbank_guess = incorrectGuessLengthHandler(wordbank_guess)
        while True:
            if (wordbank_guess.lower() in dict_list):
                break
            wordbank_guess = input("\nThe word you chose is not a valid guess please try again or leave blank for a random word\n")
            if (len(wordbank_guess) == 0):
                wordbank_guess = ''.join(random.choices(dict_list, weights=weight_list, k=1))
                break
        return wordbank_guess.lower()
    else:
        # Provides the user with a randomly selected (valid) word
        random_guess = ''.join(random.choices(dict_list, weights=weight_list, k=1))
        print("\nThis is your randomly suggested word: ", random_guess)
        return random_guess

# import wordle dictionary into a list
dict_file = open("wordle-dictionary-full.txt", "r")
dict_list = []
for line in dict_file:
    stripped_line = line.strip()
    dict_list.append(stripped_line)

# parse user input for mode of operation
parser = argparse.ArgumentParser()
parser.add_argument('--mode', metavar='<random | wordbank>', type=str, required=True)
args = parser.parse_args()
mode_str = args.mode
while True:
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
first_guess = input("What would you like your first guess to be? (leave empty for default first guess of 'audio')\n")
first_guess = incorrectGuessLengthHandler(first_guess)
if (len(first_guess) == 5):
    while (not (first_guess.lower() in dict_list)):
        first_guess = input("Your word was not found within the Wordle dictionary please enter another or leave blank to use 'audio'\n")
        if (len(first_guess) == 0):
            first_guess = 'audio'
            break
        first_guess = incorrectGuessLengthHandler(first_guess)
else:
    first_guess = 'audio'
first_guess = first_guess.lower()
print("\nPlease try <", first_guess, "> for your first guess\n")

# round 2
second_guess = subsequentRounds(first_guess)
print("\nPlease try <", second_guess, "> for your second guess\n")

# round 3
third_guess = subsequentRounds(second_guess)
print("\nPlease try <", third_guess, "> for your third guess\n")

# round 4
fourth_guess = subsequentRounds(third_guess)
print("\nPlease try <", fourth_guess, "> for your fourth guess\n")

# round 5
fifth_guess = subsequentRounds(fourth_guess)
print("\nPlease try <", fifth_guess, "> for your fifth guess\n")

# round 6
sixth_guess = subsequentRounds(fifth_guess)
print("\nPlease try <", sixth_guess, "> for your last guess\n")
