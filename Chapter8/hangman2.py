# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:09:04 2019

@author: gtdav
"""
import random

# Both of this variables are global
HANGMAN_PICS = [
    """
   +---+
       |
       |
       |
      ===""",
    """
   +---+
   0   |
       |
       |
      ===""",
    """
   +---+
   0   |
   |   |
       |
      ===""",
    """
   +---+
   0   |
  /|   |
       |
      ===""",
    """
   +---+
   0   |
  /|\  |
       |
      ===""",
    """
   +---+
   0   |
  /|\  |
  /    |
      ===""",
    """
   +---+
   0   |
  /|\  |
  / \  |
      ===""",
    """
   +---+
  [0   |
  /|\  |
  / \  |
      ===""",
    """
   +---+
  [0]  |
  /|\  |
  / \  |
      ===""",
]
words = {
    "Colors": """red orange yellow green blue indigo violet white black
         brown""".split(),
    "Shapes": """square triangle rectangle circle ellipse rhombus trapezoid
         chevron pentagon hexagon septagon octagon""".split(),
    "Fruits": """apple orange lemon lime pear watermelon grape grapefruit cherry
         banana cantaloupe mango strawberry tomato'.split(),
         Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle
         fish frog goat leech lion lizard monkey moose mouse otter owl panda
         python rabbit rat shark sheep skunk squid tiger turkey turtle weasel
         whale wolf wombat zebra""".split(),
}


# Input: a dictionary full of words
# Output: a random word from the list
def getRandomWord(wordDict):
    # This function returns a random string from the passed dictionary of
    # lists of strings and its key.
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]


# Use: display the board each time an input is made
# Input: 1st param: how many mistakes has the user made,
# 2nd param: a variable which has the letters
# already guessed and blanks where it does not,
# 3rd param: the random word the machine selected
# Output: none
def displayBoard(missedLetters, correctLetters, secretWord):
    # it selects one of the pics of the array of ASCII pics based
    # on the mistakes
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    # displays the words that the used failed already
    print("Missed letters:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    # it diplays underscores based on the lenght of the word
    blanks = "_" * len(secretWord)

    # The two following fors replace the blanks with letters already guessed
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1 :]

    for letter in blanks:
        print(letter, end=" ")
    print()


# Use: check that the used inputted a single letter or
# another one that has already been picked
# Input: the letter that the user entered, 1st param:
# a list of letters already guessed
# Output: the same letter entered
def getGuess(alreadyGuessed):
    # loops until the guess is valid
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()  # converts to lower case
        if len(guess) != 1:
            print("Please eneter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter.")
        else:
            return guess


def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


print("S U P E R  H A N G M A N")

difficulty = ""
difficulties = ["E", "M", "H"]
while difficulty not in difficulties:
    print("Enter difficulty: E - Easy, M - Medium, H - Hard")
    difficulty = input().upper()
if difficulty == "M":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == "H":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ""
correctLetters = ""
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print("The secret word is in the set: " + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"!You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(
                "You have run out of guesses!\nAfter "
                + str(len(missedLetters))
                + " missed guesses and "
                + str(len(correctLetters))
                + ' correct guesses, the word was "'
                + secretWord
                + '"'
            )
            gameIsDone = True

    # Ask the player to play again
    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
