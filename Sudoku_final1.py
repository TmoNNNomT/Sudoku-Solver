from tkinter import *
import numpy as np
import time

start = time.time()

root = Tk()
global test, sudoku
sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], ]

class CreateFrame:
    def __init__(self, root, color, w, h, row, col, cols):
        self.fr = Frame()
        self.fr = Frame(root, bg=color, width=w, height=h)
        self.fr.grid(row=row, column=col, columnspan=cols)
        self.fr.grid_propagate(FALSE)


class CreateTopFrames:
    def __init__(self, frtop, row, col):
        self.fr = Frame(frtop, bg='black', width=60, height=60)
        self.fr.grid(row=row, column=col)
        self.fr.pack_propagate(FALSE)


class CreateTopLabel:
    def __init__(self, frtop, text):
        self.lab = Label(frtop, text=text, height=1, width=3,fg='white', bg='black', font=("Comic Sans MS", 21))
        self.lab.pack(fill=BOTH, expand=1)
        self.lab.bind("<Button-1>", lambda event: updnum(event, text))


class CreateCenterFrames:
    def __init__(self, frcenter, row, col, clr):
        self.fr = Frame(frcenter, width=60, height=60, highlightbackground=clr, highlightcolor=clr, highlightthickness=2)
        self.fr.grid(row=row, column=col)
        self.fr.pack_propagate(FALSE)


class CreateCenterLabels:
    def __init__(self, fcc, m, n):
        self.lab = Label(fcc, bg='light grey', text="", font=("Comic Sans MS", 21))
        self.lab.pack(expand=1, fill=BOTH)
        self.lab.bind("<Button-1>", lambda event: updoku(event, m, n))


def updnum(event, text):
    global test
    test = text


def updoku(event, m, n):
    global test, sudoku

    sudoku[m][n] = int(test)
    # print(sudoku[m][n])
    if test == '0 ':
        test = ' '
    lc[m][n].lab.config(text=test)


def extract(event):
    a, b = list_all_legal_moves(sudoku)

    main(sudoku, b, a)



def clear(event):

    for i in range(9):
        for j in range(9):
            lc[i][j].lab.config(text=' ')
            sudoku[i][j] = 0

def display(w1):
    for i in range(9):
        for j in range(9):
            var = w1[i][j]
            lc[i][j].lab.config(text=str(var))


frameTop = CreateFrame(root, "black", 660, 60, 0, 0, 3)
frameLeft = CreateFrame(root, "black", 60, 540, 1, 0, 1)
frameCenter = CreateFrame(root, "light grey", 540, 540, 1, 1, 1)
frameRight = CreateFrame(root, "black", 60, 540, 1, 2, 1)
frameBottom = CreateFrame(root, "black", 660, 60, 2, 0, 3)

fr0 = CreateTopFrames(frameTop.fr, 0, 0)
fr1 = CreateTopFrames(frameTop.fr, 0, 1)
fr2 = CreateTopFrames(frameTop.fr, 0, 2)
fr3 = CreateTopFrames(frameTop.fr, 0, 3)
fr4 = CreateTopFrames(frameTop.fr, 0, 4)
fr5 = CreateTopFrames(frameTop.fr, 0, 5)
fr6 = CreateTopFrames(frameTop.fr, 0, 6)
fr7 = CreateTopFrames(frameTop.fr, 0, 7)
fr8 = CreateTopFrames(frameTop.fr, 0, 8)
fr9 = CreateTopFrames(frameTop.fr, 0, 9)
fr10 = CreateTopFrames(frameTop.fr, 0, 10)

L0 = CreateTopLabel(fr0.fr, '0 ')
L1 = CreateTopLabel(fr1.fr, '1 ')
L2 = CreateTopLabel(fr2.fr, '2 ')
L3 = CreateTopLabel(fr3.fr, '3 ')
L4 = CreateTopLabel(fr4.fr, '4 ')
L5 = CreateTopLabel(fr5.fr, '5 ')
L6 = CreateTopLabel(fr6.fr, '6 ')
L7 = CreateTopLabel(fr7.fr, '7 ')
L8 = CreateTopLabel(fr8.fr, '8 ')
L9 = CreateTopLabel(fr9.fr, '9 ')

fc = [[[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []], ]
lc = [[[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []],
      [[], [], [], [], [], [], [], [], []], ]

for i in range(9):
    for j in range(9):

        if (i>=0 and i<=2) and (j>=0 and j<=2):
            clr = "grey"
        elif (i>=3 and i<=5) and (j>=3 and j<=5):
            clr = "grey"
        elif (i>=6 and i<=8) and (j>=6 and j<=8):
            clr = "grey"
        elif (i>=6 and i<=8) and (j>=0 and j<=2):
            clr = "grey"
        elif (i>=0 and i<=2) and (j>=6 and j<=8):
            clr = "grey"
        else:
            clr = "black"

        fc[i][j] = CreateCenterFrames(frameCenter.fr, i, j, clr)
        lc[i][j] = CreateCenterLabels(fc[i][j].fr, i, j)

frb0 = CreateTopFrames(frameBottom.fr, 0, 0)
frb1 = CreateTopFrames(frameBottom.fr, 0, 1)
frb2 = CreateTopFrames(frameBottom.fr, 0, 2)
frb3 = CreateTopFrames(frameBottom.fr, 0, 3)
frb4 = CreateTopFrames(frameBottom.fr, 0, 4)
frb5 = CreateTopFrames(frameBottom.fr, 0, 5)
frb6 = CreateTopFrames(frameBottom.fr, 0, 6)
frb7 = CreateTopFrames(frameBottom.fr, 0, 7)
frb8 = CreateTopFrames(frameBottom.fr, 0, 8)
frb9 = CreateTopFrames(frameBottom.fr, 0, 9)
frb10 = CreateTopFrames(frameBottom.fr, 0, 10)



empty = []


def check_rows_columns_grids(puzzle, i, j):
    # check rows
    used_numbers_in_row = []
    for num in puzzle[i][:]:
        if num:
            used_numbers_in_row.append(num)

    # check columns
    used_numbers_in_column = []
    for a in range(9):
        if puzzle[a][j]:
            # if (i, j) == (0, 2):
            #     print(num, "num")
            used_numbers_in_column.append(puzzle[a][j])

    # find top left cords of  grid
    x = i//3 * 3
    y = j//3 * 3

    # check grid
    used_numbers_in_grid = []
    for a in range(3):
        x1 = x + a
        for b in range(3):
            y1 = y + b
            if puzzle[x1][y1]:
                used_numbers_in_grid.append(puzzle[x1][y1])

    # find legal numbers
    legal_numbers = []
    for a in range(1, 10):
        if a not in used_numbers_in_grid:
            if a not in used_numbers_in_column:
                if a not in used_numbers_in_row:
                    legal_numbers.append(a)
    # if (i, j) == (0, 2):
    #     print(legal_numbers,"here")
    #     print(used_numbers_in_row,"here")
    #     print(used_numbers_in_column,"here")
    #     print(used_numbers_in_grid,"here")
    return legal_numbers


def list_all_legal_moves(puzzle):
    all_legal_moves = [[[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []], ]

    num_legal = [[99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99], ]
    # find empty squares
    for a in range(9):
        for b in range(9):
            if not puzzle[a][b]:
                legal_moves_a_b = check_rows_columns_grids(puzzle, a, b)
                # legal moves at cords a, b
                all_legal_moves[a][b] = legal_moves_a_b.copy()
                num_legal[a][b] = len(legal_moves_a_b)

    return all_legal_moves, num_legal


def check_fault(puzzle, numbers):
    for a in range(9):
        for b in range(9):
            if puzzle[a][b] == 0 and numbers[a][b] == 0:
                return False

    return True


def check_win(puzzle):
    for a in range(9):
        for b in range(9):
            if puzzle[a][b] == 0:
                return False

    return True


def update_rcg(all_move, all_num, m, n, value):

    # update row and column
    for c in range(9):
        if value in all_move[m][c]:
            all_move[m][c].remove(value)
            all_num[m][c] -= 1
        if value in all_move[c][n]:
            all_move[c][n].remove(value)
            all_num[c][n] -= 1

    i1 = m // 3 * 3
    j1 = n // 3 * 3
    # update grid
    for c in range(3):
        i2 = i1 + c
        for d in range(3):
            j2 = j1 + d
            if value in all_move[i2][j2]:
                all_move[i2][j2].remove(value)
                all_num[i2][j2] -= 1
    all_num[m][n] = 99
    all_move[m][n] = empty.copy()
    return all_num, all_move


def main(puzzle, num_all_mov, mat_all_mov):
    num_all_movc = [[99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99],
                 [99, 99, 99, 99, 99, 99, 99, 99, 99], ]
    mat_all_movc = [[[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []],
                       [[], [], [], [], [], [], [], [], []], ]

    if check_fault(puzzle, num_all_mov) is False:
        return False
    if check_win(puzzle) is True:
        return True

    least = np.min(num_all_mov)
    for c in range(9):
        for d in range(9):
            if num_all_mov[c][d] == least:
                m = c
                n = d

    for value in mat_all_mov[m][n]:
        puzzle[m][n] = value

        for i in range(9):
            for j in range(9):
                num_all_movc[i][j] = num_all_mov[i][j]
                mat_all_movc[i][j] = mat_all_mov[i][j].copy()
        num_all_movc, mat_all_movc = update_rcg(mat_all_movc, num_all_movc, m, n, value)
        new = puzzle.copy()

        if main(new, num_all_movc, mat_all_movc) is True:
            display(puzzle)
            return


        puzzle[m][n] = 0

    puzzle[m][n] = 0

    return False


l1 = Label(frb2.fr, bg='light green', text="S", font=("Comic Sans MS", 21), relief="solid")
l1.pack_propagate(FALSE)
l1.pack(expand=1, fill=BOTH)
l1.bind("<Button-1>", extract)

l2 = Label(frb1.fr, bg='pink', text="AC", font=("Comic Sans MS", 21), relief="solid")
l2.pack_propagate(FALSE)
l2.pack(expand=1, fill=BOTH)
l2.bind("<Button-1>", clear)

root.mainloop()