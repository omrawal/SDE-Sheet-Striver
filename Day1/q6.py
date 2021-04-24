# merge overlaping intervals
def mergePossible(a, b):
    if(a[1] >= b[0]):
        return True

# Time O(nlogn + n)
# space O(n)


def optimal(intervals):
    n = len(intervals)
    if(n <= 1):
        return intervals

    ans = []
    intervals.sort()
    cache = intervals[0]
    for i in intervals:
        if(mergePossible(cache, i)):
            cache = [cache[0], max(cache[1], i[1])]
        else:
            ans.append(cache)
            cache = i
    ans.append(cache)
    return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(optimal(intervals))
