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
    lives = 6

    #Now we're gonna ask the user for a letter to guess
    while len(wordLetters) > 0 and lives > 0: #make them keep guessing
        print('You have', lives,'lives left\n' 'Used Letters: ', ' '.join(usedLetters)) #' '.join() puts a space inbetween all of the used letters and concatenates them into 1 string
        print()
        #Next print out what the current word is
        # put whatever letter, if it is in usedLetters, or put a - for each letter in word
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Word is', ' '.join(wordList))
        print()



        guessedLetter = input('Guess a letter:').upper()
        print()
        if (guessedLetter in alphabet) and (guessedLetter not in usedLetters) :
            usedLetters.add(guessedLetter)
            #Was it a correctly guessed letter contained in our wordLetters set or not?
            if guessedLetter in wordLetters:
                wordLetters.remove(guessedLetter)
            else:
                lives = lives - 1
                print('Letter isn\'t in word')
        elif guessedLetter in usedLetters:
            print('You already guessed that letter! Try again')

        #Invalid input
        else:
            print('Not a letter in the alphabet, c\'mon')


    if lives == 0:
        print('Loser, sorry! The word was', word)
    else:
        print('You got it! The word was', word, '!')

hangman()