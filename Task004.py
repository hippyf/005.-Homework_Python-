# Создайте программу для игры в "Крестики-нолики"

from os import system

def PrintField (field):				
	print('  a b c')
	for i in range(len(field)):
		print(i + 1, end = ' ')
		print(*field[i])

def ActionToIndex(field, action):	
	rowSymb = ['1', '2', '3']
	columnSymb = ['a', 'b', 'c']
	for i in range(len(rowSymb)):
		for j in range(len(columnSymb)):
			if action == rowSymb[i] + columnSymb[j]:
				if field[i][j] == '*':	return [i, j]
	return False

def WinnerCheck(field):		
	winner = 0
	if field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X':	winner = 1
	elif field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X':	winner = 1
	elif field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X':	winner = 1
	elif field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X':	winner = 1
	elif field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X':	winner = 1
	elif field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X':	winner = 1
	elif field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X':	winner = 1
	elif field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X':	winner = 1

	elif field[0][0] == '0' and field[0][1] == '0' and field[0][2] == '0':	winner = 2
	elif field[1][0] == '0' and field[1][1] == '0' and field[1][2] == '0':	winner = 2
	elif field[2][0] == '0' and field[2][1] == '0' and field[2][2] == '0':	winner = 2
	elif field[0][0] == '0' and field[1][0] == '0' and field[2][0] == '0':	winner = 2
	elif field[0][1] == '0' and field[1][1] == '0' and field[2][1] == '0':	winner = 2
	elif field[0][2] == '0' and field[1][2] == '0' and field[2][2] == '0':	winner = 2
	elif field[0][0] == '0' and field[1][1] == '0' and field[2][2] == '0':	winner = 2
	elif field[0][2] == '0' and field[1][1] == '0' and field[2][0] == '0':	winner = 2
	
	return winner


field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
maxSteps = 9
countSteps = 0
flagWinner = False
gamer = 0			
winner = 0			
action = ''

system('cls')
print('Пример ввода хода: 1a, 2b и т.д.')
print()
PrintField(field)
print()

while countSteps < maxSteps and not flagWinner:
	if gamer:
		action = input('Ход игрока 2 (нолики): ')
		if ActionToIndex(field, action):
			field[ActionToIndex(field, action)[0]][ActionToIndex(field, action)[1]] = '0'
			system('cls')
			print('Пример ввода хода: 1a, 2b и т.д.')
			print()
			PrintField(field)
			print()
			countSteps += 1
		else:
			print('Недопусимый ход! Пропуск хода!')
	else:
		action = input('Ход игрока 1 (крестики): ')
		if ActionToIndex(field, action):
			field[ActionToIndex(field, action)[0]][ActionToIndex(field, action)[1]] = 'X'
			system('cls')
			print('Пример ввода хода: 1a, 2b и т.д.')
			print()
			PrintField(field)
			print()
			countSteps += 1
		else:
			print('Недопусимый ход! Пропуск хода!')
	
	if WinnerCheck(field):
		winner = WinnerCheck(field)
		flagWinner = True
	
	gamer = int(not gamer)

system('cls')
PrintField(field)
print()
if winner == 1:		print('Победил игрок 1 (крестики)')
elif winner == 2:	print('Победил игрок 2 (нолики)')
else:				print('Ничья')