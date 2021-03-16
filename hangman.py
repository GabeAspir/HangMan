import random
from words import words
import string

#Inspired by Kylie Ying on YouTube
#This is my first foray into python, I usually do Java

def getValidWord(words):
    word = random.choice(words) #Randomly chooses a word from words.py
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    #Now we're gonna ask the user for a letter to guess
    guessedLetter = input('Guess a letter:').upper()
    if (guessedLetter in alphabet) and (guessedLetter not in usedLetters) :
        usedLetters.add(guessedLetter)
        #Was it a correctly guessed letter contained in our wordLetters set or not?
        if guessedLetter in wordLetters:
            wordLetters.remove(guessedLetter)

    elif guessedLetter in usedLetters:
        print('You already guessed that letter! Try again')

    #Invalid input
    else:
        print('Not a letter in the alphabet, c\'mon')

userInput = input('Type something:')
print(userInput)