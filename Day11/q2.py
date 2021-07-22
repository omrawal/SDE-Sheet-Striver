# median of a sorted matrix


def brute(A):
    m = len(A)
    n = len(A[0])
    lst = list()
    for i in range(m):
        for j in range(n):
            lst.append(A[i][j])
    lst.sort()
    k = len(lst)//2
    return lst[k]


A = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]
# print(brute(A))

# Time O(n*m + m*nlogn*m)
# Space O(n*m)


def countSmallerThanEqualToMid(row, mid):
    l = 0
    h = len(row)-1
    while(l <= h):
        middle = l+(h-l)//2
        if(row[middle] <= mid):
            l = middle+1
        else:
            h = middle-1
    return l


def optimal(A):
    low = 1
    high = 1e9
    n = len(A)
    m = len(A[0])
    while(low <= high):
        mid = low+(high-low)//2
        count = 0  # count of numbers <= mid
        for i in range(n):
            count += countSmallerThanEqualToMid(A[i], mid)
        if(count <= (n*m)/2):
            low = mid-1
    return low
