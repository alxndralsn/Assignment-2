# Alexandra Lesan
# 2433764

# Function already given
def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

# Part 1
import random
import sys

def tileLabels(n):
    tiles = []
    for i in range(1, n**2):
        tiles.append(str(i))
    tiles.append('  ')
    return tiles

def getNewPuzzle(n):
    puzzle = []
    tiles = tileLabels(n)
    random.shuffle(tiles)
    for i in range(n):
        sublist = []
        for j in range(n):
            sublist.append(tiles.pop(0))
            if len(sublist[j]) == 1:
                sublist[j] += ' '
        puzzle.append(sublist)
    return puzzle

def findEmptyTile(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle)):
            if puzzle[row][col] == '  ':
                return (row, col)

def nextMove(puzzle):
    empty = findEmptyTile(puzzle)
    n = len(puzzle)
    possible = [' ', ' ', ' ', ' ']
    if empty[0] != (n-1):
        possible[0] = 'W'
    if empty[0] != 0:
        possible[1] = 'S'
    if empty[1] != (n-1):
        possible[2] = 'A'
    if empty[1] != 0:
        possible[3] = 'D'
    
    valid = False
    while not valid:
        move = input(f'                          ({possible[0]})\nEnter WASD (or QUIT): ({possible[2]}) ({possible[1]}) ({possible[3]})\n')
        if move.upper() in possible:
            valid = True
        elif move.lower() == 'quit':
            print('Until next time!')
            sys.exit()
        else:
            print('Invalid input!')
            
    return move.upper()


# Part 2
def makeMove(puzzle, move):
    (e_row, e_col) = findEmptyTile(puzzle)
    if move == 'W':
        puzzle[e_row][e_col], puzzle[e_row+1][e_col] = puzzle[e_row+1][e_col], puzzle[e_row][e_col]
    elif move == 'S':
        puzzle[e_row][e_col], puzzle[e_row-1][e_col] = puzzle[e_row-1][e_col], puzzle[e_row][e_col]
    elif move == 'A':
        puzzle[e_row][e_col], puzzle[e_row][e_col+1] = puzzle[e_row][e_col+1], puzzle[e_row][e_col]
    elif move == 'D':
        puzzle[e_row][e_col], puzzle[e_row][e_col-1] = puzzle[e_row][e_col-1], puzzle[e_row][e_col]

def solved(puzzle, n):
    sorted_puzzle = []
    tiles = tileLabels(n)
    for i in range(n):
        sublist = []
        for j in range(n):
            sublist.append(tiles.pop(0))
            if len(sublist[j]) == 1:
                sublist[j] += ' '
        sorted_puzzle.append(sublist)
    return puzzle == sorted_puzzle

# Main program
print('''Hello! Welcome to the sliding puzzle game!
You are given an n x n tile board, where one of the tiles is empty and all other tiles are integers.
The objective is to obtain an increasing sorted order of the tiles from left to right and top to bottom.
This is done by continuously sliding the tiles. 
Tiles can only slide to an adjacent empty cell. 
Possible valid moves are: left, right, up, down. 
''')

n = int(input('Please input the dimension of the board (n): '))
print()

puzzle = getNewPuzzle(n)
print('Here is your board! ')
displayBoard(puzzle)
print()

moves = 0
Done = False
while not Done:
    move = nextMove(puzzle)
    makeMove(puzzle, move)
    displayBoard(puzzle)
    moves += 1

    Done = solved(puzzle, n)

if n == 3:
    if moves <= 31:
        print(f'Congratulations! You solved it in {moves} moves!')
    else:
        print(f'You solved the puzzle, but did it in {moves} moves...')
        print('Best of luck next time!')
elif n == 4:
    if moves <= 80:
        print(f'Congratulations! You solved it in {moves} moves!')
    else:
        print(f'You solved the puzzle, but did it in {moves} moves...')
        print('Best of luck next time!')
else:
    print(f'Congratulations! You solved it in {moves} moves!')