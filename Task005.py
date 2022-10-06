# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from os import system

system('cls')

def StrToRLE (stroka):
	result = ''
	flagRepeatingElement = False
	count = 1
	for i in range(len(stroka)):
		if i != len(stroka) - 1:
			if stroka[i] == stroka[i + 1]:
				flagRepeatingElement = True
				count += 1
			else:
				if flagRepeatingElement:
					result += f'{count}' + stroka[i]
					flagRepeatingElement = False
				else:
					result += stroka[i]
				count = 1
		else:
			if flagRepeatingElement:
				result += f'{count}' + stroka[i]
			else:
				result += stroka[i]
	return result

def IsNumber (symbol):
	numberList = [str(i) for i in range(10)]
	for i in numberList:
		if symbol == i:
			return True
	return False

def RLE_ToStr (stroka):
	result = ''
	num = ''
	flagNumber = False
	cycle = 0
	for i in range(len(stroka)):
		if IsNumber(stroka[i]):
			num = num + stroka[i]
			flagNumber = True
		else:
			if flagNumber:
				for j in range(int(num)):
					result += stroka[i]
				num = ''
				flagNumber = False
			else:
				result += stroka[i]
	return result

data = open('in.txt', 'r')
inputStr = []
for line in data:
	inputStr.append(line)
data.close()

data = open('compressed.txt', 'w')
for i in inputStr:
	data.write(StrToRLE(i))
data.close

data = open('compressed.txt', 'r')
compressedStr = []
for line in data:
	compressedStr.append(line)
data.close()

data = open('decompressed.txt', 'w')
for i in compressedStr:
	data.write(RLE_ToStr(i))
data.close