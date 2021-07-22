# number of subarrays with given XOR

# brute O(n^3)
# better O(n^2)


def better(arr, x):
    n = len(arr)
    count = 0
    for i in range(n):
        cumm_xor = 0
        for j in range(i, n):
            cumm_xor = cumm_xor ^ arr[j]
            if(cumm_xor == x):
                count += 1
    return count


# arr = [5, 6, 7, 8, 9]
# x = 5

# print(better(arr, x))


def optimal(arr, x):
    hashMap = {}
    count = 0
    xor = 0
    n = len(arr)
    for i in range(n):
        xor ^= arr[i]
        if(xor ^ x in hashMap):
            count += hashMap[xor ^ x]
        if(xor == x):
            count += 1
        # if()
