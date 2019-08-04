import random

guessesTaken = 0
cont = 'y'

myName = input('Hola hola, ¿cómo te llamas?\n')

number = random.randint(1,20)
print(f'Bueno, {myName}, estoy pensando en un numero entre el 1 y el 20...')
print('A ber, atínale. Tienes 5 intentos')

while cont in ['y','Y']:
	for guessesTaken in range(5):
		guess = input()
		guess = int(guess)
	
		if guess < number:
			print('Nope, muy bajo.')
		
		if guess > number:
			print('Nope, muy alto.')
		
		if guess == number:
			break
	
		restantes = 5 - 1 - guessesTaken
	
		if restantes != 0:
			print (f'The quedan {restantes} intentos.')
		
	if guess == number:
		guessesTaken = str(guessesTaken + 1)
		if guessesTaken != '5':
			print (f'¡Muy bien {myName}, le atinaste en {guessesTaken} intentos! :D')
		else:
			print (f'Uff, en el último intento, muy bien {myName}.')
	
	if guess != number:
		number = str(number)
		print (f'Estaba pensando en {number}. Chale.')

	cont = input('¿Jugar de nuevo? (Y/N) ')
	print (cont)
	
	
	if cont in ['y','Y']:
		print("Va, de nuevo, tienes 5 intentos.")
		int(guessesTaken)
		guessesTaken = 0
		number = random.randint(1,20)
		
#Note to self: if you do an if statement with strings use 'in'
