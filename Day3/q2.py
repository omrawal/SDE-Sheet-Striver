# pow(x,n)
# brute


def myPow(x: float, n: int) -> float:
    nflag = False
    if(n == 0):
        return 1
    else:
        if(n < 0):
            nflag = True
        res = 1
        for i in range(abs(n)):
            res *= x
        if(nflag):
            return 1/res
        else:
            return res

# gives overflow hence need to give a better approach

# optimal


def mypow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    pow = 1
    while n:
        if n % 2 == 1:
            pow *= x
        x *= x
        n //= 2
    return pow


print(mypow(2.00000, -2))
