# 4 sum

# brute
# sort -> 3 pointer -> binary search

# time O(n^3 logn+ nlogn)
# space O(1)


def brute(nums, target):
    n = len(nums)
    nums.sort()
    ans = []
    print(nums)
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                find = target-(nums[i]+nums[j]+nums[k])
                low = k+1
                high = n-1
                found = False
                while(low <= high):
                    # print(low, high)
                    mid = (low+(high))//2
                    if(find == nums[mid]):
                        found = True
                        break
                    elif(nums[mid] < find):
                        low = mid+1
                    else:
                        high = mid-1
                if(found):
                    a = [nums[i], nums[j], nums[k], find]
                    ans.append(a)
    return ans


# nums = [1, 0, -1, 0, -2, 2]
# target = 0
# print(brute(nums, target))


# optimal

def optimal(nums, target):
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    ans = []
    for i in range(0, n):
        for j in range(i+1, n):
            new_target = target-nums[i]-nums[j]
            front = j+1
            back = n-1
            while(front < back):
                two_sum = nums[front]+nums[back]
                if(two_sum < new_target):
                    front += 1
                elif(two_sum > new_target):
                    back -= 1
                else:
                    a = []
                    a.append(nums[i])
                    a.append(nums[j])
                    a.append(nums[front])
                    a.append(nums[back])
                    if(a not in ans):
                        ans.append(a)
                    while(front < back and nums[front] == a[2]):
                        front += 1
                    while(front < back and nums[back] == a[3]):
                        back -= 1
    return ans


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(optimal(nums, target))
