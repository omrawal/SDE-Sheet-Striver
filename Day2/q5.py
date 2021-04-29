# Buy sell stock


def brute(arr):
    n = len(arr)
    start = -1
    end = -1
    max_profit = 0
    for i in range(n):
        curr_sum = arr[i]
        for j in range(i+1, n):
            max_profit = max(max_profit, arr[j]-curr_sum)
        # max_profit = max(max_profit, curr_sum)
    return max_profit


# arr = [7, 6, 4, 3, 1]
# print(brute(arr))
