# 3 Sum
# all triplets whose sum is 0

# Brute
# Loop n^3


def brute(nums):
    ans = []
    n = len(nums)
    if(n < 3):
        return ans
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(nums[i]+nums[j]+nums[k] == 0):
                    l = sorted([nums[i], nums[j], nums[k]])
                    if l not in ans:
                        ans.append(l)
    return ans

# Time O(n^3 log m) log m == removing duplicates
# space O(m)

# better
# Hashing


def better(nums):
    ans = set()
    count_dict = {}
    n = len(nums)
    if(n < 3):
        return []

    # creating count Dict
    for i in nums:
        if(i in count_dict):
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    # checking for triplets
    # print(count_dict)
    for i in range(n):
        count_dict[nums[i]] -= 1
        for j in range(i+1, n):
            count_dict[nums[j]] -= 1
            target = (-1*(nums[i]+nums[j]))
            if(target in count_dict and count_dict[target] > 0):
                found = [nums[i], nums[j], target]
                found.sort()
                ans.add(tuple(found))
            count_dict[nums[j]] += 1
        count_dict[nums[i]] += 1
    return list(ans)


# time O(n^2 log m)
# space O(m)


# optimal 2 pointer approach
# to ignore duplicates hint is sort the array

def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res
