# Minimum platforms required
# sort both arrival and departure time
# no need to care of sequence as we just need max platforms occupied simultaneously


def minPlatform(n, arr, dep):
    if(n < 2):
        return n
    arr.sort()
    dep.sort()
    platform_needed = 0
    result = 0
    i = 0
    j = 0
    while(i < n and j < n):
        if(arr[i] <= dep[j]):
            platform_needed += 1
            i += 1
        else:
            platform_needed -= 1
            j += 1
        result = max(result, platform_needed)
    return result

# Time O(nlogn + nlogn)
# space O(1)
