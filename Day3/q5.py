# grid unique paths


# a = [[0]*cols]*rows

# bruteforce
# Recursion tree approach
def brute(i, j, m, n):
    if(i == m-1 and j == n-1):
        return 1
    elif(i >= m or j >= n):
        return 0
    else:
        return brute(i+1, j, m, n)+brute(i, j+1, m, n)


# print(brute(0, 0, 3, 2))


# better
# time O(n*m)
# space O(n*m)


def better(i, j, m, n):
    global dp
    # print(dp, i, j)
    if(i == m-1 and j == n-1):
        return 1
    if(i >= m or j >= n):
        return 0
    if(dp[i][j] != -1):
        return dp[i][j]
    else:
        dp[i][j] = better(i+1, j, m, n)+better(i, j+1, m, n)
        return dp[i][j]


m = 3
n = 7
dp = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(-1)
    dp.append(a)

# print(better(0, 0, m, n))


# optimal
# there are always finite steps we take to reach
# (n+m-2)C(m-1)  or (n+m-2)C(n-1)

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)


def nCr(n, r):
    return fact(n)/(fact(r)*fact(n-r))


def optimalrec(i, j, m, n):
    return nCr(n+m-2, m-1)

# time O(m-1) or O(n-1)
# space O(1)


def optimal(m, n):
    N = n+m-2
    R = m-1
    # nCr logic
    res = 1
    for i in range(1, R+1):
        res *= (N-R+i)/i
    return round(res)


# print(optimalrec(0, 0, 3, 3))
print(optimal(3, 2))
