#!/usr/bin/python3
# sudoku_show_read_file.py

def display_game(game_str):
	outline=''
	if len(game_str)!=82:
		return False
	for x in range(0,9):
		if x==3 or x==6:
			print()
		outline=''
		for y in range(0,9):
			index=x*9+y
			if index%3==0:
				outline+='  '
			char=game_str[index]
			if char=='0':
				char='_'
			outline+=char+' '
		print(outline)
	return True

#Read a file
with open("sudoku_1EI.txt","rt",newline="\n") as game_file:
	line1=game_file.readline()
	line2=game_file.readline()
	print('game line1')
	if not display_game(line1):
		print('line1 failed')
	print()
	print('game line2')
	if not display_game(line2):
		print('line2 failed')
