# Subset 2

# brute
# sebsets using pick not pick method and put them in sets to get unique ones

# 2^n  2^nlog 2^n

ansList = []


def rec(self, ind, nums, ds):
    self.ansList.add(tuple(ds.copy()))
    for i in range(ind, len(nums)):
        if(i != ind and nums[i] == [i-1]):
            continue
        ds.append(nums[i])
        self.rec(i+1, nums, ds)
        ds.pop(-1)


def optimal(nums):
    nums.sort()
    ansList = []
    rec(ins=0, nums=nums, ds=[], ans=ansList)
    return ansList
