#!/usr/bin/env python3

"""
    sudoku_solver.py
    2020
"""



class Board:
    def __init__(self, data):
        self._data = [v for row in data for v in row]
        self._static_digits_index = {i for i,v in enumerate(self._data) if v is not None}

    def __str__(self):
        chars = []
        for i in range(9):
            for j in range(9):
                item = self[i,j]
                chars.append(f"{item}" if item is not None else '_')
                chars.append('_' if i%3 == 2 else ' ')
                if j%3 == 2:
                    chars.append('|')
            chars.append('\n')
        return ''.join(chars)

    def __getitem__(self, coord):
        return self._data[coord[0]*9+coord[1]]

    def __setitem__(self, coord, value):
        index = coord[0]*9+coord[1]
        if index in self._static_digits_index:
            raise ValueError("Cannot change number an initial number.")
        self._data[index] = value


    def is_available(self, coord):
        """ Returns true if the coordinate is a valid slot (not one of the initial digits). """
        return coord[0]*9+coord[1] not in self._static_digits_index

    def get_digits_available(self, coord):
        """ Returns all the digits available for the coord, considering sudoku's rules. """
        ii, jj = coord
        block_start_i = (ii//3)*3 # rounds ii down to either 0, 3 or 6
        block_start_j = (jj//3)*3 # rounds jj down to either 0, 3 or 6
        digits_in_block = set(
            self[y,x]
            for y in range(block_start_i, block_start_i + 3)
            for x in range(block_start_j, block_start_j + 3)
        )
        digits_in_row = set(self[ii,x] for x in range(9))
        digits_in_column = set(self[y,jj] for y in range(9))
        return set(range(1, 10)) - (digits_in_block | digits_in_column | digits_in_row)



def next_coord(coord):
    """ Returns `next` coordinate (i, j) in grid. 
            (... -> (1, 8) -> (2, 0) -> (2, 1) -> ...)
        If coord is the last one, it returns (9, 0) as opposed to wrapping around to (0, 0).
    """
    return (coord[0] + (coord[1]==8), (coord[1] + 1) % 9)


def recursion_solve(board, coord=(0, 0)):
    """ Solves sudoku board using brute-force backtracking algorithm """
    if coord == (9, 0):
        return True

    if board.is_available(coord):
        nums = board.get_digits_available(coord)
        while nums:
            board[coord] = nums.pop()
            result = recursion_solve(board, next_coord(coord))
            if result:
                return True
        board[coord] = None
        return False
    else:
        return recursion_solve(board, next_coord(coord))



def main():
    test1 = [[4,8,9,None,None,5,None,None,None],
             [7,None,2,None,4,6,8,3,None],
             [None,None,6,None,None,None,None,4,9],
             [8,7,3,None,6,None,None,None,5],
             [None,2,None,None,8,1,None,6,3],
             [1,None,5,4,7,None,9,None,8],
             [None,None,None,None,None,None,None,8,None],
             [None,3,None,6,None,None,1,5,7],
             [None,None,None,8,1,None,None,None,6]]


    board = Board(test1)

    print(board)
    recursion_solve(board)
    print(f"Solved board:\n\n{board}")

if __name__ == "__main__":
    main()
