import random
from words import words
import string

#Inspired by Kylie Ying on YouTube

def getValidWord(words):
    word = random.choice(words) #Randomly chooses a word from words.py
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

userInput = input('Type something:')
print(userInput)