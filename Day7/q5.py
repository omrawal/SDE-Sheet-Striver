# max consecutive ones


def firstApproach(nums):
    n = len(nums)
    if(n < 1):
        return 0
    max_occur = 0
    curr_occur = 0
    for i in range(n):
        if(nums[i] == 1):
            curr_occur += 1
            max_occur = max(curr_occur, max_occur)
        elif(nums[i] == 0):
            curr_occur = 0
    return max_occur

# Fist approach
# Time O(n)
# space O(1)
