# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:23:31 2019

@author: David García
"""

import random
number1 = random.randint(1,10)
number2 = random.randint(1,10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if int(answer) == number1 + number2:
	print('Correct!')
else:
	print('Nope! The answer is ' + str(number1 + number2))