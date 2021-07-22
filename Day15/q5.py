# Longest Common Prefix

# Time O(n*m)
# where n is size is list
# m is average size of each word
# Space O(1)

# Brute


def longestCommonPrefix(self, strs) -> str:
    ans = ''
    ans_pointer = 0
    n = len(strs)
    flag = True
    if(n == 1):
        return strs[0]
    while(flag and ans_pointer < len(strs[0])):
        if(len(strs[0]) < 1):
            flag = False
            break
        target = strs[0][ans_pointer]
        for i in range(1, n):
            if(ans_pointer >= len(strs[i]) or strs[i][ans_pointer] != target):
                flag = False
                break
        if(not flag):
            break
        ans_pointer += 1
        ans += target
    return ans

# Optimal is trie
