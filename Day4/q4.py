# Largest subarray with sum 0

# Brute
# For loops


def maxLen(n, arr):
    max_count = 0
    for left in range(0, n):
        for right in range(left+1, n):
            curr_count = 0
            curr_sum = 0
            for i in range(left, right+1):
                curr_sum += arr[i]
                curr_count += 1
            if(curr_sum == 0):
                max_count = max(max_count, curr_count)
    return max_count

# Time O(n^3)
# Space O(1)

# optimal
# using hash map


def maxLen(n, arr):
    hashMap = {}
    curr_sum = 0
    max_count = 0
    for i in range(n):
        curr_sum += arr[i]
        if(curr_sum == 0):
            max_count = max(i+1, max_count)
        else:
            if(curr_sum in hashMap):
                max_count = max(max_count, abs(hashMap[curr_sum]-i))
            else:
                hashMap[curr_sum] = i

    return max_count


# Time O(nlogn)
# Space O(n)
