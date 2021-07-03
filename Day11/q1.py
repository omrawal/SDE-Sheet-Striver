# Nth root of an integer using Binary search

# finding nth root of m
# i.e. if m==27 and n==3 than ans is 3


def findRoot(n, m):
    low = 1
    high = m
    if(n == 1):
        return m
    eps = 1e-6
    while((high-low) > eps):
        mid = (low+high)/2.0
        if(mid**n < m):
            low = mid
        else:
            high = mid
    return("{:.2f}, {:.2f}".format(low, high))


m = 5
n = 2
print(findRoot(n, m))
