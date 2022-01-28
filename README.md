# Wordle-Assistant

## Description

*currently a work-in-progress project*

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

With the knowledge of what words are considered "legal", I'm designing a program that
will assist the user in guessing the correct word. There will be two methods: random
word generator and word bank generator. The first will use information from previous
guesses to generate a random word from the Wordle dictionary that fits the criteria
and will either help your progress or will be the answer. The latter will generate a
list of words (or word bank) that contains all the words that fit the criteria based
on previous guesses and allow the user to choose which word they want to submit to
Wordle.

## Requirements

- Python 3.5 or above
- (maybe some pip packages, TBD)

## How-to

(This is not an in-browser tool, it'll have to be run on a command line that can execute Python programs)

To execute this program, using your preferred python equipped terminal inside the root directory of this
repository [Wordle-Assistant](https://github.com/Wang-Derr/Wordle-Assistant) and run:
`python3 wordle_solver.py --mode <random | wordbank>`.
From there, simply follow the prompts and you'll be on your way to (*hopefully*) solving your daily
Wordle challenge!
