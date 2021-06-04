# Search in 2D Matrix

# brute
# Time O(NxM)


def brute(mat, key):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(n):
            if(mat[i][j] == key):
                return True
    return False

# better 1
# Time O(nlog m)


def better1(mat, key):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        # binary search
        left = 0
        right = n-1
        while(left < right):
            mid = (left+(right-left))//2
            if(mat[i][mid] == key):
                return True
            elif(mat[i][mid] > key):
                right = mid-1
            else:
                left = mid+1
    return False


# better 2
# Time O(n+m)
def better2(mat, key):
    m = len(mat)
    n = len(mat[0])
    i = 0
    j = n-1
    while((0 <= i < m) and (0 <= j < n)):
        # print(i, j)
        if(mat[i][j] == key):
            return True
        elif(mat[i][j] < key):
            i += 1
        elif(mat[i][j] > key):
            j -= 1
    return False


# Optimal
# Time O(log(n+m))
def optimal(mat, target):
    m = len(mat)
    n = len(mat[0])
    low = 0
    high = m*n-1
    while(low <= high):
        mid = (low+(high-low))//2  # WOW no int overflow
        i = mid//n
        j = mid % n
        if(mat[i][j] == target):
            return True
        elif(mat[i][j] < target):
            low = mid+1
        elif(mat[i][j] > target):
            high = mid-1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
# print(better1(matrix, target))
# print(better2(matrix, target))
print(optimal(matrix, target))
