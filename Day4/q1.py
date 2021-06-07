# 2 sum

# brute
# n^2 complexity


def brute(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i != j):
                if(nums[i]+nums[j] == target):
                    return([i, j])


# optimal
# hash table
# time O(n)
# space O(n)
def better(nums, target):
    count_dict = {}
    n = len(nums)
    for i in range(n):
        k = target-nums[i]
        if k in count_dict:
            return [count_dict[k], i]
        else:
            count_dict[nums[i]] = i
    return []


nums = [3, 2, 4]
target = 6
print(better(nums, target))
