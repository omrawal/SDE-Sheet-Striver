# median of two sorted arrays

import math
# Brute


def brute(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    newlist = []
    i = 0
    j = 0
    while(i < l1 and j < l2):
        if(nums1[i] < nums2[j]):
            newlist.append(nums1[i])
            i += 1
        else:
            newlist.append(nums2[j])
            j += 1

    while(i < l1):
        newlist.append(nums1[i])
        i += 1
    while(j < l2):
        newlist.append(nums2[j])
        j += 1

    if((l1+l2) % 2 == 0):
        m1 = math.floor((l1+l2)/2)
        m2 = m1-1
        return (newlist[m1]+newlist[m2])/2
    else:
        return newlist[math.floor((l1+l2)/2)]

# time O(n+m)
# space O(n+m)

# better is instead of new space O(n) maintain a counter and take uptill n+m/2
