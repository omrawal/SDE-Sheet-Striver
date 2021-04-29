# Buy sell stock

# Time O(n^2)
# Space O(1)


def brute(arr):
    n = len(arr)
    # start = -1
    # end = -1
    max_profit = 0
    for i in range(n):
        curr_sum = arr[i]
        for j in range(i+1, n):
            max_profit = max(max_profit, arr[j]-curr_sum)
        # max_profit = max(max_profit, curr_sum)
    return max_profit


# arr = [7, 6, 4, 3, 1]
# print(brute(arr))


# Time O(n)
# Space O(1)
def optimal(arr):
    min_val = 1000001
    profit = 0
    n = len(arr)
    for i in range(n):
        min_val = min(min_val, arr[i])
        profit = max(profit, arr[i]-min_val)
    return profit


arr = [7, 1, 5, 3, 6, 4]

print(optimal(arr))
