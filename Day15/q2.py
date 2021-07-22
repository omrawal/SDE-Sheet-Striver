# longest Palindrome

# brute Time O(n^3)


def checkPalindrome(self, start, end, s):
    while(start <= end):
        if(s[start] != s[end]):
            return False
        start += 1
        end -= 1
    return True


def longestPalin(self, S):
    # code here

    flag = 0
    ans = ''
    for i in range(0, len(S)):
        for j in range(i, len(S)):
            if(self.checkPalindrome(i, j, S)):
                if(j-i+1 > len(ans)):
                    ans = S[i:j+1]
    return ans

# Optimal
# dynamic programming approach techdose
# not working refer nick white

# def optimal(S):
#     # creating dp matrix
#     # not working
#     n = len(S)
#     dp = [[None for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if(i == j):
#                 dp[i][j] = 1
#             elif(abs(j-i) == 1):
#                 if(S[i] == S[j]):
#                     dp[i][j] = 1
#                 else:
#                     dp[i][j] = 0
#     max_start = 0
#     max_end = 0
#     for i in range(n):
#         for j in range(n):
#             if(dp[i][j] is None):
#                 # checking palindrome
#                 if(S[i] == S[j]and i+1 < n and j-1 > 0 and dp[i+1][j-1] == 1):
#                     dp[i][j] = 1
#                     if(abs(j-i) > abs(max_end-max_start)):
#                         max_start = min(i, j)
#                         max_end = max(i, j)
#     return S[max_start: max_end+1]

# Time O(n^2)


def optimal(s):
    n = len(s)
    if(n <= 1):
        return s
    start = 0
    end = 0
    for i in range(0, n):
        # racecar
        len1 = expandFromMiddle(i, i, s)
        # abba
        len2 = expandFromMiddle(i, i+1, s)
        total_len = max(len1, len2)
        if(total_len > end-start):
            start = i-((total_len-1)//2)
            end = i+((total_len)//2)

    return s[start:end+1]


def expandFromMiddle(left, right, s):
    n = len(s)
    if(n <= 0 or left > right):
        return 0
    while(left >= 0 and right < n and s[left] == s[right]):
        left -= 1
        right += 1
    return (right - 1) - (left + 1) + 1


# s = 'forgeeksskeegfor'
# print(optimal(s))
