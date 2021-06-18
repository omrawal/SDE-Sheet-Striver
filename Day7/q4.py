# remove duplicates from sorted array

# brute
# create a new list and add onlu unique elements


def brute(nums):
    n = len(nums)
    # edge case
    if(n < 2):
        return n
    new_list = []
    new_list.append(nums[0])
    for i in range(1, n):
        if(nums[i] != new_list[-1]):
            new_list.append(nums[i])
    nums[:] = new_list
    return len(new_list)

# time O(n)
# space O(n)

# Optimal
# two pointer approach


def optimal(nums):
    n = len(nums)
    # edge case
    if(n < 2):
        return n
    left = 0
    current = 1
    while(current < n):
        if(nums[left] != nums[current]):
            nums[left+1] = nums[current]
            left += 1
            current += 1
        else:
            current += 1
    return left+1

# Time O(n)
# space O(1)
