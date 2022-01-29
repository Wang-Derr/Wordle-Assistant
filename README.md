# Wordle-Assistant

## Description

A tool to assist you in solving the daily [Wordle](https://www.powerlanguage.co.uk/wordle/) challenge. 

Wordle is a word guessing game where the goal is to guess the correct 5-letter word.
It has straightforward rules: each guess must be a 5-letter word, upon each guess
you will be notified whether a letter within your guessed word matches with a letter
within the correct word, if a letter in your guessed doesn't show up in the correct
word it'll be colored gray, if a letter you guessed is in the word but in the wrong
place it'll be colored yellow, and if you guessed a letter correctly and in the
right place it will be colored green. You only have 6 guesses.

The one rule not stated by the game is which words are valid words. Looking through
the Javascript of the game there are two lists of words: a smaller list consisting of
words that could be the answer and a larger list consisting of allowable 5 letter words
that will never be the answer. They are mutually exclusive. Both lists have been
combined to generate the file `wordle-dictionary-full.txt` so that it can be used to
determine what words are possible entries without giving away which words are the most
likely answers.

With the knowledge of what words are considered "legal", I've designed a program that
will assist the user in guessing the correct word. There are two methods: random
word generator and word bank generator. The first will use information from previous
guesses to generate a random word from the Wordle dictionary that fits the established
criterion and will help you progress or might even be the answer. The latter will
generate a list of words (word bank) that contains all the words that fit the
criterion based on previous guesses and allow the user to choose which word they want
to use for Wordle.

## Requirements

- Python 3.5 or above

## How-to

(This is not an in-browser tool, it'll have to be run on a command line that can execute Python programs)

To execute this program, using your preferred python equipped terminal inside the root directory of this
repository `/Wordle-Assistant/` and run:
`python3 wordle_solver.py --mode <random | wordbank>` (pick between `random` or `wordbank` mode).
From there, simply follow the prompts and you'll be on your way to (*hopefully*) solving your daily
Wordle challenge!

This tool can also be tested against [Absurdle](https://qntm.org/files/wordle/) a Wordle inspired
adverserial word guessing game (not my work, credit belongs to [qntm](https://qntm.org/)).

## Future additions planned

- Sort (and prioritize) words by unique letters, so the wordbank list will put **tummy** before **mummy** in the wordbank because it has less repeat letters and therefore help eliminate more possibilities. This extends to the random suggestion pool, it will prioritize words with more unique letters than not when making suggestions.

## Versions

V1.0.0
- Official release!
- Two modes: random and wordbank (read description above for more details)