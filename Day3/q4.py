# Majority element II

import math
# Brute
# time O(n^2)
# space O(N)


def brute(nums):
    n = len(nums)
    target = math.floor(n/3)
    ans = set()
    for i in range(n):
        ele = nums[i]
        count = 0
        for j in range(i, n):
            if(nums[j] == ele):
                count += 1
        if(count > target):
            ans.add(ele)
    return list(ans)


# nums = [1, 2]

# print(brute(nums))

# better
# time O(n+n)
# space O(n)


def better(nums):
    n = len(nums)
    target = math.floor(n/3)
    count_dict = dict()
    ans = []
    for i in nums:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for i in count_dict:
        if(count_dict[i] > target):
            ans.append(i)
    return ans


# nums = [1, 2]

# print(better(nums))


# optimal
# boyer moore element
# atmost 2 majority greater than n/3 floor


def optimal(nums):
    num1 = num2 = -1
    c1 = c2 = 0
    n = len(nums)
    # left out
