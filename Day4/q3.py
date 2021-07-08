# longest consecutive sequence

# brute force
# Sorting


def brute(nums):
    n = len(nums)
    if(n <= 1):
        return n
    nums.sort()
    max_len = 0
    curr_len = 1
    for i in range(1, n):
        if(nums[i] == nums[i-1]+1):
            curr_len += 1
        elif(nums[i] == nums[i-1]):
            curr_len = curr_len
        else:
            curr_len = 1
        max_len = max(max_len, curr_len)

    return max_len

# Time O(nlogn +n)
# speace O(1)


# Optimal using hash set

def optimal(nums):
    hashSet = set()
    max_occur = 0
    for i in nums:
        hashSet.add(i)
    for i in nums:
        if(i-1 in hashSet):
            continue
        else:
            count = 1
            while(True):
                if(i+1 in hashSet):
                    count += 1
                else:
                    break
            max_occur = max(max_occur, count)
    return max_occur

# Time O(n+ n+ n) == O(n)
# Space O(1)
