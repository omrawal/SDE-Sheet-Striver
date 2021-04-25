# next permutation


def reverse(a, start, end):
    while(start < end):
        a[start], a[end] = a[end], a[start]
        end -= 1
        start += 1
    return a


def optimal(a):
    n = len(a)
    i = n-2
    if(n == 1):
        return a
    while(i >= 0 and a[i] >= a[i+1]):
        i -= 1
    if(i >= 0):
        j = n-1
        while(a[j] <= a[i]):
            j -= 1
        a[j], a[i] = a[i], a[j]
    return reverse(a, i+1, n-1)


current_perm = [3, 2, 1]
print(optimal(current_perm))
