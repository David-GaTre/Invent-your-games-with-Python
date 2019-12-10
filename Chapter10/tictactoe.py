# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:49:02 2019

@author: gtdav
"""
import random

def drawBoard(board):
	# This funcrion prints out the board that it was passed
	#"board is a list of 10 strings
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])
	
def inputPlayerLetter():
	# Lets the player type which letter they want to be.
	# Return a list with the player's letter as the first
	# item and the computer's letter as the second.
	letter = ''
