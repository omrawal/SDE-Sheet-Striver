# majority element

import math

# bruteforce
# original will be O(n^2)


def brute(arr):
    n = len(arr)
    count = math.floor(n/2)
    count_dict = {}
    for i in arr:
        if(i in count_dict):
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for i in count_dict:
        if(count_dict[i] > count):
            return i


# nums = [2, 2, 1, 1, 1, 2, 2]
# print(brute(nums))


# optimal
# moore's voting algo
def optimal(nums):
    n = len(nums)
    count = 0
    ele = None
    for i in range(n):
        if(count == 0):
            ele = nums[i]
        if(ele == nums[i]):
            count += 1
        else:
            count -= 1
    return ele


nums = [3, 3, 4]
print(optimal(nums))
