# find cycle in linkedlist

# brute
# create a hashtable and while inserting check if already exist


def brute(head):
    temp = head
    count_dict = {}
    while(temp != None):
        if(temp in count_dict):
            return True
        count_dict[temp] = 1
        temp = temp.next
    return False

# Time O(n)
# Space O(n)

# Optimal
# slow and fast pointer approach


def optimal(head):
    slow = fast = head
    while(slow != None and fast != None):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False

# Time O(n)
# Space O(1)
