# Merge two sorted arrays in O(1) space


import math

# Time O(n)+O(n)
# Space (N)


def brute(arr1, arr2):
    i = 0
    j = 0
    new_arr = []
    n1 = len(arr1)
    n2 = len(arr2)

    while(i < n1 and i < n2):
        if(arr1[i] < arr2[j]):
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    while(i < n1):
        new_arr.append(arr1[i])
        i += 1

    while(j < n2):
        new_arr.append(arr2[j])
        j += 1

    i = 0
    j = 0
    k = 0

    while(i < n1):
        arr1[i] = new_arr[k]
        i += 1
        k += 1

    while(j < n2):
        arr2[j] = new_arr[k]
        j += 1
        k += 1

    return (arr1, arr2)


a1 = [1, 3, 5, 7]
a2 = [0, 2, 6, 8, 9]

# print(brute(a1, a2))


# Space O(1)
# Time O(nxm)
def better(arr1, arr2):
    i = 0
    j = 0
    n1 = len(arr1)
    n2 = len(arr2)
    while(i < n1):
        if(arr1[i] > arr2[j]):
            arr1[i], arr2[j] = arr2[j], arr1[i]
            arr2.sort()
        i += 1

    # while(i < n1):
    #     for j in range(0, n2):
    #         if(arr1[i] > arr2[j]):
    #             arr1[i], arr2[j] = arr2[j], arr1[i]
    #             if(arr2[j] > arr2[j+1]):
    #                 temp = arr2[j]
    #                 k = j+1
    #                 while(k < n2 and arr2[k] > temp):
    #                     arr2[k-1] = arr2[k]
    #                     k += 1
    #                 arr2[k-1] = temp
    #                 break
    #     i += 1

    return (arr1, arr2)


# a1 = [1, 4, 7, 8, 10]
# a2 = [2, 3, 9]
# print(a1, a2)
# print(better(a1, a2))


def optimal(a1, a2):
    n1 = len(a1)
    n2 = len(a2)
    gap = math.ceil((n1+n2)/2)
    # shell sort like gap method


a1 = [1, 4, 7, 8, 10]
a2 = [2, 3, 9]
print(a1, a2)
print(optimal(a1, a2))
