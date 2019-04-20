import numpy as np

sudoku = np.array(
    [[1, 2, 3, 6, 7, 8, 9, 4, 5],
     [5, 8, 4, 2, 3, 9, 7, 6, 1],
     [9, 6, 7, 1, 4, 5, 3, 2, 8],
     [3, 7, 2, 4, 6, 1, 5, 8, 9],
     [6, 9, 1, 5, 8, 3, 2, 7, 4],
     [4, 5, 8, 7, 9, 2, 6, 1, 3],
     [8, 3, 6, 9, 2, 4, 1, 5, 7],
     [2, 1, 9, 8, 5, 7, 4, 3, 6],
     [7, 4, 5, 3, 1, 6, 8, 9, 2]])


def sudokutest(board):
    if all(np.unique(sudoku) == [1,2,3,4,5,6,7,8,9]):
        if (np.sum(board, axis=0) == 45).all() and (np.sum(board, axis=1) == 45).all():
            for y in range(0, 7, 3):
                for x in range(0, 7, 3):
                    if np.sum(board[y:y + 3, x:x + 3]) != 45:
                        return False
            return True
    return False

print(sudokutest(sudoku))
