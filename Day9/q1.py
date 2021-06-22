# Subset Sum
# recursion whether to select that element or not


def rec(self, ind, sum, arr, n, ans_set):
    if(ind == n):
        ans_set.append(sum)
        return
    # selecting the  current element for sum
    self.rec(ind+1, sum+arr[ind], arr, n, ans_set)

    # not selecting the element for sum
    self.rec(ind+1, sum, arr, n, ans_set)


def subsetSums(self, arr, N):
    ans_set = []
    self.rec(0, 0, arr, N, ans_set)
    ans_set.sort()
    return ans_set

# Time O(2^n + 2^n log 2^n)
# Space O(2^n)
