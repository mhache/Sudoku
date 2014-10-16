#!/usr/bin/python3
# sudoku_read_file.py

#Read a file
with open("sudoku_1EI.txt","rt") as game_file:
	line1=game_file.readline()
	line2=game_file.readline()

print(line1)
print(line2)
