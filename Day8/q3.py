# job Sequencing problem
# sort in descending order of profit
# maintain an array to keep a count of the job.id and time on which they are performed


def JobScheduling(self, Jobs, n):
    Jobs.sort(key=lambda i: i.profit, reverse=True)
    # Jobs.sort(key=lambda i:i.deadline)
    m = 0
    for i in Jobs:
        m = max(m, i.deadline)
    job_log = [None]*m
    total_profit = 0
    job_count = 0
    for i in Jobs:
        for j in range(i.deadline-1, -1, -1):
            # free slot
            if(job_log[j] == None):
                job_log[j] = i.id
                total_profit += i.profit
                job_count += 1
                break
    return(job_count, total_profit)


# Time = O(n logn) + O(m*n)
# Space = O(m)
