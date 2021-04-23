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


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(brute(matrix))
