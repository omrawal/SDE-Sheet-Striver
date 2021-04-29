# Rotate Image

# Bruteforce
# Time O(n^2)
# Space O(n^2)


def brute(mat):
    m = len(mat)
    n = len(mat[0])
    new_mat = []
    for i in range(m):
        new_mat.append([None]*n)
    # print(new_mat)

    for i in range(m):
        for j in range(n):
            new_mat[j][n-i-1] = mat[i][j]
    return new_mat


# brute([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])


def transpose(mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat


# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# Optimal
# Transpose and reverse each row
def optimal(mat):
    m = len(mat)
    n = len(mat[0])
    mat = transpose(mat)
    for i in range(m):
        a = 0
        b = n-1
        while(a < b):
            mat[i][a], mat[i][b] = mat[i][b], mat[i][a]
            a += 1
            b -= 1
    return mat


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(optimal(mat))
