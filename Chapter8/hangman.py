# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:09:04 2019

@author: gtdav
"""
import random
#Both of this variables are global
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   0   |
       |
       | 	
      ===''', '''
   +---+
   0   |
   |   |
       |
      ===''', '''
   +---+
   0   |
  /|   |
       |
      ===''', '''
   +---+
   0   |
  /|\  |
       |
      ===''', '''
   +---+
   0   |
  /|\  |
  /    |
      ===''', '''
   +---+
   0   |
  /|\  |
  / \  |
      ===''' ]
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra'''.split()
#Input: a list full of words
#Output: a random word from the list
def getRandomWord(wordList):
	wordIndex = random.randint(0,len(wordList) - 1)
	return wordList[wordIndex]


#Use: display the board each time an input is made
#Input: 1st param: how many mistakes has the user made, 2nd param: a variable which has the letters
#already guessed and blanks where it does not, 3rd param: the random word the machine selected
#Output: none
def displayBoard(missedLetters, correctLetters, secretWord):
	#it selects one of the pics of the array of ASCII pics based on the mistakes
	print(HANGMAN_PICS[len(missedLetters)])
	print()
	
	#displays the words that the used failed already
	print('Missed letters:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()
	
	#it diplays underscores based on the lenght of the word
	blanks = '_' * len(secretWord)
	
	#The two following fors replace the blanks with letters already guessed
	for i in range(len(secretWord)) :
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			
	for letter in blanks:
		print(letter, end= ' ')
	print()
	
#Use: check that the used inputted a single letter or another one that has already been picked
#Input: the letter that the user entered, 1st param: a list of letters already guessed
#Output: the same letter entered
def getGuess(alreadyGuessed):
	#loops until the guess is valid
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower() #converts to lower case
		if len(guess) != 1:
			print('Please eneter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a letter.')
		else:
			return guess
	
def playAgain():
	print('Do you want to play again? (yes or no)')
	return input().lower().startswith('y')

print('S U P E R  H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(missedLetters, correctLetters, secretWord)
	
	#Let the player enter a letter
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		#Check if the player has won.
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
		
		#Check if player has lost
		if len(missedLetters) == len(HANGMAN_PICS) - 1:
			displayBoard(missedLetters, correctLetters, secretWord)
			print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) 
			+ ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"' )
			gameIsDone = True
			
	#Ask the player to play again
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break