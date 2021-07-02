# sodoku


def isValid(row, col, matrix, val):
    # sudoku grid always 9x9

    # check row
    for i in range(9):
        if(matrix[i][col] == str(val)):
            return False
    # check col
    for i in range(9):
        if(matrix[row][i] == str(val)):
            return False
    # check for box
    x1 = (row//3)*3
    y1 = (col//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if(matrix[x1+i][y1+j] == str(val)):
                return False
    return True


def smartIsValid(row, col, matrix, val):
    for i in range(0, 9):
        # checking rows
        if(matrix[i][col] == str(val)):
            return False
        # checking cols
        if(matrix[row][i] == str(val)):
            return False
        # checking 3x3 square
        if(matrix[3*(row//3)+i//3][3*(col//3)+i % 3] == str(val)):
            return False


def solve(matrix):
    for i in range(9):
        for j in range(9):
            if(matrix[i][j] == '.'):
                for val in range(1, 10):
                    if(isValid(i, j, matrix, val)):
                        matrix[i][j] = str(val)
                        if(solve(matrix)):
                            return True
                        else:
                            # got false so remove the previously filled value
                            matrix[i][j] = '.'
                # not posssible to place anyting from 1-9
                return False
    # no empty cell found Sudoku is completely solved
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(solve(board))
print(board)
