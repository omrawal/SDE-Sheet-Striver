# Subset 2

# brute
# sebsets using pick not pick method and put them in sets to get unique ones

# 2^n  2^nlog 2^n

# Incorrect


def rec(ind, nums, ds, ans):
    ans.append(ds)
    for i in range(ind, len(nums)):
        if(i != ind and nums[i] == [i-1]):
            continue
        ds.append[nums[i]]
        rec(ind=i+1, nums=nums, ds=ds, ans=ans)
        ds.pop(-1)


def optimal(nums):
    nums.sort()
    ansList = []
    rec(ins=0, nums=nums, ds=[], ans=ansList)
    return ansList
