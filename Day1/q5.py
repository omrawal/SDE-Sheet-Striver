# maximum subarray sum kadane's algo

# time O(N^3)


def brute(arr):
    n = len(arr)
    if(n == 1):
        return arr[0]
    max_sum = -9999999
    for i in range(n):
        for j in range(i, n):
            max_sum = max(max_sum, sum(arr[i:j+1]))
    return max_sum


# a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# # a = [1]
# a = [5, 4, -1, 7, 8]
# print(brute(a))


# time O(n^2)
def better(arr):
    n = len(arr)
    max_sum = -999999
    for i in range(n):
        sumi = 0
        for j in range(i, n):
            sumi += arr[j]
        max_sum = max(max_sum, sumi)
    return max_sum


# a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# a = [1]
# a = [5, 4, -1, 7, 8]
# print(better(a))


# kadane's Algo
# Time O(n)
def optimal(arr):
    n = len(arr)
    max_sum = 0
    curr_sum = 0
    for i in range(n):
        curr_sum += arr[i]
        if(curr_sum < 0):
            curr_sum = 0
        max_sum = max(max_sum, curr_sum)
    return max_sum


# a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# a = [1]
a = [5, 4, -1, 7, 8]
print(optimal(a))
