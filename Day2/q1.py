# pascal's triangle


def optimal(n):
    ans = []
    prev_row = None
    for i in range(n):
        a = []
        for j in range(0, i+1):
            if(j == 0 or j == i):
                a.append(1)
            else:
                a.append(prev_row[j-1]+prev_row[j])
        prev_row = a
        ans.append(a)
    return ans


n = 5
print(optimal(5))
