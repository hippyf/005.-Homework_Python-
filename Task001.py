# Игра с конфетами человек против человека.
# На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

from os import system
from random import randint

system('cls')

candiesOnTable = 2021
candiesLimit = 28
candiesGamers = [0, 0]
gamer = randint(0, 1)	
print(f'Первым ходит игрок {gamer + 1}')
winner = 0

while candiesOnTable:
	candies = int(input(f'Сколько конфет забирает игрок {gamer + 1}?: '))
	if candies > candiesLimit:	candies = candiesLimit
	elif candies < 1:			candies = 1

	if candies >= candiesOnTable:
		candiesOnTable = 0
		winner = gamer
	else:
		candiesGamers[gamer] += candies
		candiesOnTable -= candies
		gamer = int(not gamer)

print(f'Победил игрок {winner + 1}')