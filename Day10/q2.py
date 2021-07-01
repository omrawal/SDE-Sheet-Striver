# N queens problem

# queen no. is same as row no. +1
# matric is chess board


def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_mat = []
    for j in range(col):
        temp = []
        for i in range(row):
            temp.append(matrix[i][j])
        new_mat.append(temp)

    return new_mat


def isSafe(row, col, matrix):
    # as checking for newly placed queen is best decision
    # we only check if the newly added queen is under attack
    # Q denotes Queen
    # as matrix is nxn

    # queens can only be in N,W,NW dirs

    # North
    r = row-1
    c = col
    while(r >= 0):
        if(matrix[r][c] == 'Q'):
            return False
        r -= 1

    # West
    r = row
    c = col-1
    while(c >= 0):
        if(matrix[r][c] == 'Q'):
            return False
        c -= 1

    # North West
    r = row-1
    c = col-1
    while(c >= 0 and r >= 0):
        if(matrix[r][c] == 'Q'):
            return False
        c -= 1
        r -= 1
    return True


# matrix = [
#     '....',
#     '..Q.',
#     '....',
#     '....'
# ]
# matrix = [['.']*4]*4
# print(matrix)
# print(isSafe(1, 2, matrix))
# print(matrix[2][0])

def nqueen(n):
    matrix = [['.']*n]*n
    for i in range(0, n):
        pass
