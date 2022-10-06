
#Добавьте игру против бота

from os import system
from random import randint

system('cls')

candiesOnTable = 2021
candiesLimit = 28
candiesGamers = [0, 0]
gamer = randint(0, 1)
if gamer:	print('Первым ходит бот')
else:		print('Первым ходит игрок')
winner = 0

while candiesOnTable:
	if gamer:
		candies = randint(1, candiesLimit)
		print(f'Бот забирает конфет:  {candies}')
	else:
		candies = int(input('Сколько конфет забирает игрок?: '))

	if candies > candiesLimit:	candies = candiesLimit
	elif candies < 1:			candies = 1

	if candies >= candiesOnTable:
		candiesOnTable = 0
		winner = gamer
	else:
		candiesGamers[gamer] += candies
		candiesOnTable -= candies
		gamer = int(not gamer)

if winner:	print('Победил бот')
else:		print('Победил игрок')