# duplicate number in array of size N+1


def bruteForce(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if(arr[i] == arr[j]):
                return arr[i]


arr1 = [1, 3, 4, 2, 2]
arr2 = [3, 1, 3, 4, 2]
arr3 = [1, 1]

print(bruteForce(arr1))
print(bruteForce(arr2))
print(bruteForce(arr3))
