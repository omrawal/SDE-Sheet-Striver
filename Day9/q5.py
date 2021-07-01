# palindrome Partitioning


class Solution:
    def isPalindrome(self, arr, start, end):
        while(start <= end):
            if(arr[start] != arr[end]):
                return False
            start += 1
            end -= 1
        return True

    def rec(self, index, s, path, res):
        if(index == len(s)):
            res.append(path.copy())
            return
        for i in range(index, len(s)):
            if(self.isPalindrome(s, index, i)):
                path.append(s[index:i+1])
                self.rec(i+1, s, path, res)
                path.pop(-1)

    def partition(self, s: str):
        res = []
        path = []
        self.rec(0, s, path, res)
        return res

# Time O(2^n)
# Space O(n)
