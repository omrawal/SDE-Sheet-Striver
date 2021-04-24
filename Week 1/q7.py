# set matrix zeroes


def brute(matrix):
    rows = []
    cols = []
    n_row = len(matrix)
    n_col = len(matrix[0])
    for i in range(n_row):
        for j in range(n_col):
            if(matrix[i][j] == 0):
                rows.append(i)
                cols.append(j)
    for i in range(n_row):
        for j in range(n_col):
            if(i in rows or j in cols):
                matrix[i][j] = 0
    return matrix


# matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# print(brute(matrix))

def optimal(matrix):
    cols = True
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        if(matrix[i][0] == 0):
            cols = False
        for j in range(col):
            if(matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(row-1, -1, -1):
        for j in range(col-1, 0, -1):
            if(matrix[i][0] == 0 or matrix[0][j] == 0):
                matrix[i][j] = 0
        if(cols == False):
            matrix[i][0] = 0
    return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(optimal(matrix))
