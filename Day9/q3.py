class Solution:
    ans = []

    def rec(self, index, target, nums, ds):
        if(index == len(nums)):
            if(target == 0):
                self.ans.append(ds.copy())
            return
        # select

        if(target >= nums[index]):
            ds.append(nums[index])
            self.rec(index, target-nums[index], nums, ds)
            ds.pop(-1)
        # reject
        self.rec(index+1, target, nums, ds)

    def combinationSum(self, candidates, target: int):
        self.ans = []
        self.rec(0, target, candidates, [])
        return self.ans

# Time O(2^t * k)
# Space O(k*x)
