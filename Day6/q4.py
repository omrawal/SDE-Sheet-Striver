# check panindrome Linked List

# brute
# transfer to array and check in array
# Time O(n+n)
# Space O(n)

# optimal
# Find middle of linkedlist using two pointer (fast and slow method)
# Reverse the second half using the dummy node method
# traverse these both parts simultaneously and check equality


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head: ListNode) -> bool:
    # find middle
    slow = fast = head
    while(fast != None and fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    # reverse second half
    newhead = slow.next
    dummy = None

    while(newhead != None):
        next = newhead.next
        newhead.next = dummy
        dummy = newhead
        newhead = next
    slow.next = dummy
    t2 = slow.next
    t1 = head
    while(t2 != None):
        if(t1.val != t2.val):
            return False
        t1 = t1.next
        t2 = t2.next
    return True


# Time O(n/2)+O(n/2)+O(n/2)+O(n/2)
# Space O(1)
