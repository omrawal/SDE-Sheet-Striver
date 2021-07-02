# N queens problem

# queen no. is same as row no. +1
# matric is chess board
# import copy


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


def modifyCopy(matrix):
    n = len(matrix)
    new_mat = []

    for i in range(n):
        res = ''
        for j in range(n):
            res += matrix[i][j]
        new_mat.append(res)
    return new_mat


def isSafe(row, col, matrix):
    # as checking for newly placed queen is best decision
    # we only check if the newly added queen is under attack
    # Q denotes Queen
    # as matrix is nxn
    n = len(matrix)
    # queens can only be in N,W,NW dirs

    # North
    r = row-1
    c = col
    while(r >= 0):
        if(matrix[r][c] == 'Q'):
            return False
        r -= 1

    # North West
    r = row
    c = col
    while(c >= 0 and r >= 0):
        if(matrix[r][c] == 'Q'):
            return False
        c -= 1
        r -= 1

    # West
    r = row
    c = col
    while(c >= 0):
        if(matrix[r][c] == 'Q'):
            return False
        c -= 1

    # South West
    r = row
    c = col
    while(r < n and c >= 0):
        if(matrix[r][c] == 'Q'):
            return False
        r += 1
        c -= 1

    # # North East
    # r = row+1
    # c = col+1
    # while(c < n and r < n):
    #     if(matrix[r][c] == 'Q'):
    #         return False
    #     c += 1
    #     r += 1

    return True


def solve(col, matrix, ans):
    n = len(matrix)
    if(col == n):
        # all queens are places and are safe
        # ans.append(matrix.copy())
        ans.append(modifyCopy(matrix))
        # print(matrix.copy())
        return
    for row in range(0, n):
        if(isSafe(row, col, matrix)):
            # new queen safe so place it
            matrix[row][col] = 'Q'
            # print(row, col)
            solve(col+1, matrix, ans)
            # no safe place in this column for current placement backtrack
            matrix[row][col] = '.'


def nqueen(n):
    # matrix = [['.']*n]*n
    matrix = [['.' for i in range(n)] for j in range(n)]
    ans = list()
    solve(0, matrix, ans)
    return ans


print(nqueen(4))


# k = [['.', '.', 'Q', '.'], ['Q', '.', '.', '.'],
#      ['.', '.', '.', 'Q'], ['.', 'Q', '.', '.']]

# print(modifyCopy(k))


# matrix = [
#     '....',
#     '..Q.',
#     '....',
#     '....'
# ]
# matrix = [
#     ['Q', '.', '.', '.'],
#     ['.', '.', '.', '.'],
#     ['.', '.', '.', '.'],
#     ['.', '.', '.', '.']
# ]
# print(matrix)
# print(isSafe(1, 0, matrix))
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         print(i, j, matrix[i][j])
