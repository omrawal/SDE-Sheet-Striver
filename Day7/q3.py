# Trapping Rainwater Problem

# brute

# height at any index is min( max(left), max(right) ) - current height


def brute(height):
    total_water = 0
    n = len(height)
    # no gap to capture water
    if(n < 3):
        return total_water

    for i in range(1, n-1):
        # get max to left
        max_left = max(height[0:i])
        # get max to right
        max_right = max(height[i+1:])
        total_water += max(0, min(max_left, max_right)-height[i])
    return total_water

# Time O(n*n)
# space O(1)

# better
# maintain prefix_max and suffix_max array to avoid n^2 time complexity


def optimal(height):
    total_water = 0
    n = len(height)
    # no gap to capture water
    if(n < 3):
        return total_water
    prefix_max = [None]*n
    suffix_max = [None]*n
    # filling prefix max
    for i in range(n):
        if(i == 0):
            prefix_max[i] = max(0, height[i])
        else:
            prefix_max[i] = max(prefix_max[i-1], height[i])

    # filling suffix max
    for i in range(n-1, -1, -1):
        if(i == n-1):
            suffix_max[i] = max(0, height[i])
        else:
            suffix_max[i] = max(suffix_max[i+1], height[i])

    # Calculating water trapped
    for i in range(1, n-1):
        total_water += max(0, min(suffix_max[i], prefix_max[i])-height[i])
    return total_water

# Time O(n+n+n)==O(n)
# Space O(n+n)==O(n)

# Optimal
# two pointer approach
# left and right pointer


def optimal(height):
    total_water = 0
    n = len(height)
    # no gap to capture water
    if(n < 3):
        return total_water
    left = 0
    right = n-1
    leftMax = 0
    rightMax = 0
    while(left <= right):
        if(height[left] <= height[right]):
            # is there a block to left greater?
            if(height[left] >= leftMax):
                leftMax = height[left]
            else:
                # water can be trapped
                total_water += leftMax-height[left]
            left += 1
        else:
            # is there a block to right greater?
            if(height[right] > rightMax):
                rightMax = height[right]
            else:
                # water can be trapped
                total_water += rightMax-height[right]
            right -= 1
    return total_water

# Time O(n)
# space O(1)
