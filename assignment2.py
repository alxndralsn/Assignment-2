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

# Functions to implement
import random
import sys

def tileLabels(n):
    tiles = []
    for i in range(1, (n**2)):
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

def findEmptyTile(puzzle):
    for row in range(len(puzzle)):
        for elem in range(len(puzzle)):
            if puzzle[row][elem] == '  ':
                return (row, elem)

def nextMove(puzzle):
    empty = findEmptyTile(puzzle)
    n = len(puzzle)
    possible = [w, a, s, d] = [' ', ' ', ' ', ' ']
    if empty[0] != 0:
        w = 'W'
    if empty[0] != (n-1):
        s = 'S'
    if empty[1] != 0:
        a = 'A'
    if empty[1] != (n-1):
        d = 'D'
    
    valid = False
    while not valid:
        move = input(f'                          ({w})\nEnter WASD (or QUIT): ({a}) ({s}) ({d})\n')
        if move.upper() in possible:
            valid = True
        elif move.lower() == 'quit':
            sys.exit()
        else:
            print('Invalid input!')
            
    return move.upper()

nextMove(getNewPuzzle(4))