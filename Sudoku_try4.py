import numpy as np
import time
start = time.time()
sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 6, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 0, 0, 4, 5, 7, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8],
          [0, 0, 8, 5, 0, 0, 0, 1, 0],
          [0, 9, 0, 0, 0, 0, 4, 0, 0], ]
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

        if main(puzzle, num_all_movc, mat_all_movc) is True:
            for jj in puzzle:
                print(jj)
            end = time.time()
            print(end - start)
            exit()

        puzzle[m][n] = 0

    puzzle[m][n] = 0

    return False


a, b = list_all_legal_moves(sudoku)
main(sudoku, b, a)

