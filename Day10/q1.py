# print all permutations of string or array
class Solution:
    def rec(self, sinput, soutput, ans):
        if(sinput == []):
            ans.append(soutput.copy())
            return
        n = len(sinput)
        for i in range(n):
            k = sinput.pop(i)
            self.rec(sinput, soutput+[k], ans)
            sinput.insert(i, k)

    def permute(self, nums):
        ans = []
        soutput = []
        self.rec(nums, soutput, ans)
        return ans

# Time O(n! * n)
# Space O(n+n)

# Approach 2


class Solution:

    def rec(self, sinput, index, ans):
        n = len(sinput)
        if(index == n-1):
            ans.append(sinput.copy())
            return

        for i in range(index, n):
            sinput[i], sinput[index] = sinput[index], sinput[i]
            self.rec(sinput, index+1, ans)
            sinput[i], sinput[index] = sinput[index], sinput[i]

    def permute(self, nums):
        ans = []
        index = 0
        self.rec(nums, index, ans)
        return ans

# Time O(n! *n)
# Space O(n+1)
