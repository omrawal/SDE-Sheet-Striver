# n meetings 1 room


def soln(n, start, end):
    meetings = []
    final_ans = []
    for i in range(n):
        meetings.append((start[i], end[i], i+1))
    meetings.sort(key=lambda item: item[1])
    for i in meetings:
        if(len(final_ans) == 0):
            final_ans.append(i)
        else:

            if(final_ans[-1][1] < i[0] and final_ans[-1][0] < i[0]):
                final_ans.append(i)
    # print(final_ans)
    return len(final_ans)

# Time O(n)+ O(nlogn)+ O(n) == O(n)
# Space O(n)
