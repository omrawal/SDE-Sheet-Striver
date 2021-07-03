# Rat in aa maze

# Visited is boolean matrix tracking to visited blocks

# some test cases are failed
import copy


def solve(row, col, matrix, visited, output, ans):
    n = len(matrix)
    if(row == n-1 and col == n-1):
        ans.add(copy.deepcopy(output))
        return
    # D
    if(row+1 < n and (not visited[row+1][col]) and matrix[row+1][col] == 1):
        visited[row+1][col] = True
        solve(row+1, col, matrix, visited, output+'D', ans)
        visited[row+1][col] = False
    # L
    if(col-1 >= 0 and (not visited[row][col-1]) and matrix[row][col-1] == 1):
        visited[row][col-1] = True
        solve(row, col-1, matrix, visited, output+'L', ans)
        visited[row][col-1] = False
    # R
    if(col+1 < n and (not visited[row][col+1]) and matrix[row][col+1] == 1):
        visited[row][col+1] = True
        solve(row, col+1, matrix, visited, output+'R', ans)
        visited[row][col+1] = False
    # U
    if(row-1 >= 0 and (not visited[row-1][col]) and matrix[row-1][col] == 1):
        visited[row-1][col] = True
        solve(row-1, col, matrix, visited, output+'U', ans)
        visited[row-1][col] = False


def findPath(m, n):
    ans = set()
    visited = [[False for i in range(n)]for j in range(n)]
    if(m[0][0] == 1):
        solve(0, 0, m, visited, '', ans)
    if(len(ans) == 0):
        return -1
    return ans


m = [[1, 1],
     [1, 1]]

n = len(m)

print(findPath(m, n))
