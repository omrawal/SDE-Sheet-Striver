# reverse pairs

# bruteforce
# Time O(n^2)
# Space O(1)


def brute(nums):
    n = len(nums)
    pair_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if(nums[i] > 2*nums[j]):
                pair_count += 1
    return pair_count


# print(brute([2, 4, 3, 5, 1]))

# better
