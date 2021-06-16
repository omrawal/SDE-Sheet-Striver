# Rotate Linked list

# brute
# Rotate k times one node to right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 0
        t = head
        while(t != None):
            n += 1
            t = t.next
        k = k % n
        for i in range(k):
            t1 = head
            while(t1.next.next != None):
                t1 = t1.next
            temp = t1.next
            t1.next = None
            temp.next = head
            head = temp
        return head

# Time O(n*k+n)
# Space O(1)


# Optimal
# find length of linkedlist in O(n)
# point last's next to head so that list is now circular
# k=k%n
# k=n-k
# traverse k nodes ahead point its next to null and make its next node as head

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = 0
        t = head
        while(t.next != None):
            n += 1
            t = t.next
        n += 1
        t.next = head
        k = n-k
        for i in range(k):
            t = t.next
        head = t.next
        t.next = None
        return head


# Time O(n+ n-(n%k)) ==O(n)
# Space O(1)
