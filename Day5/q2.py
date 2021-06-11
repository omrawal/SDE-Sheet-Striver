# find middle of linked list

# brute force
# time O(n+n/2)
# space O(n) or if twice traversal without array than O(1)
import math


def brute(head):
    arr = []
    temp = head
    while(temp != None):
        arr.append(temp.val)
        temp = temp.next
    n = len(arr)
    k = math.ceil(n/2)
    if(n % 2 == 0):
        k += 1
    temp = head
    for i in range(1, k):
        temp = temp.next
    return temp


# optimal
# tortoise method 2 pointer slow and fast pointer approach
# time O(n/2)
# space O(1)
def optimal(head):
    slow = fast = head
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow
