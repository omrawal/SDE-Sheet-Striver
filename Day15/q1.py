# reverse words in a string


def reverseWords(s):
    s_list = list(s)
    if(len(s_list) <= 1):
        return s
    n = len(s)
    # removing spaces

    left = 0
    curr = 0
    flag = False
    while(curr < n):
        if(s_list[curr] != ' '):
            s_list[curr], s_list[left] = s_list[left], s_list[curr]
            left += 1
            # print(curr, curr+1, s[curr], s[curr+1])
            if(curr+1 < n and s_list[curr+1] == ' '):
                flag = True
                left += 1
        curr += 1
    s = s_list[:left]
    while(s[-1] == ' '):
        s = s[:left-1]
    # reversing complete string
    left = 0
    right = len(s)-1
    while(left <= right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    # reversing words between spaces
    left = 0
    right = 0
    curr = 0
    while(curr < len(s)-1):
        if(s[curr+1] == ' '):
            right = curr
            while(left <= right):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            left = curr+2
        curr += 1
    right = curr
    while(left <= right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)


s = "  hello world  "
print(reverseWords(s))


# Time O(n+n+n) ==O(n)
# Space O(1)
