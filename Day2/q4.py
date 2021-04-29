# inversion of array
# [8,4,2,1] -> 6

# time = appoximate O(N^2)


def brute(a):
    n = len(a)
    inversion_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if(a[j] < a[i]):
                inversion_count += 1
    return inversion_count


a = [1, 1, 3, 4, 5, 6, 8]
# print(brute(a))


def mergeSort(arr):
    global inv_count
    n = len(arr)
    if(n > 1):
        mid = n//2
        left = arr[:mid]
        right = arr[mid:n]
        mergeSort(left)
        mergeSort(right)

        # merge
        i = j = k = 0
        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                inv_count += (mid-i)
                k += 1
                j += 1
        while(i < len(left)):
            arr[k] = left[i]
            k += 1
            i += 1
        while(j < len(right)):
            arr[k] = right[j]
            k += 1
            j += 1


# uses merge sort technique
# Time O(n log n)
# space O(n)

inv_count = 0


def optimal(a):
    n = len(a)
    global inv_count
    mergeSort(a)
    return inv_count


arr = [8, 4, 2, 1]
# mergeSort(arr)

# print(arr)
print(optimal(arr))


# arr = [1, 20, 6, 4, 5]
