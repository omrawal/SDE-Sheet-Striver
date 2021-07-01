# kth permutation sequence

# Brute
# Using recursion generate all sequences
# sort them
# returh k-1 th index

# Time O(n! *n + n! logn!)
# space O(n)


# optimal
# mathematical approach

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = math.factorial(n-1)
        numbers = [i for i in range(1, n+1)]
        ans = ''
        k -= 1
        while(True):
            # pick number and add it to our answer
            ans += str(numbers[k//fact])
            numbers.pop(k//fact)
            if(numbers == []):
                break
            k = k % fact
            fact = fact//len(numbers)
        return ans
