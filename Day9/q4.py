class Solution:
    ans = set()

    def rec(self, index, nums, target, ds):
        if(target == 0):
            self.ans.add(tuple(ds.copy()))
            return
        for i in range(index, len(nums)):
            if(i != index and nums[i] == [i-1]):
                continue
            if(nums[i] > target):
                break
            ds.append(nums[i])
            self.rec(i+1, nums, target-nums[i], ds)
            ds.pop(-1)

    def combinationSum2(self, candidates, target: int):
        self.ans = set()
        candidates.sort()
        self.rec(0, candidates, target, [])
        return self.ans
# gives TLE
