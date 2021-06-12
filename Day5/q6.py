# Add 2 numbers given as linkedlist

# bruteforce
# Time O(n+m)+ O(n+m)
# Space O(n+m)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def brute(self, l1: ListNode, l2: ListNode) -> ListNode:
    n1 = ''
    n2 = ''
    t1 = l1
    t2 = l2
    while(t1 != None):
        n1 += str(t1.val)
        t1 = t1.next
    while(t2 != None):
        n2 += str(t2.val)
        t2 = t2.next
    n1 = n1[::-1]
    n2 = n2[::-1]
    n1 = int(n1)
    n2 = int(n2)
    ans = n1+n2
    ans = str(ans)
    ans = ans[::-1]
    newhead = None
    curr = None
    for i in ans:
        newNode = ListNode(int(i))
        if(newhead == None):
            newhead = newNode
            curr = newhead
        else:
            curr.next = newNode
            curr = newNode
    return newhead


# Optimal
# Time O(n+m)
# Space O(n+m)

def Optimal(self, l1: ListNode, l2: ListNode) -> ListNode:
    t1 = l1
    t2 = l2
    carry = 0
    newHead = None
    curr = None
    while(t1 != None and t2 != None):
        ans = t1.val+t2.val+carry
        if(ans > 9):
            carry = int(str(ans)[0])
            value = int(str(ans)[1])
        else:
            value = int(str(ans)[0])
            carry = 0
        newNode = ListNode(value)
        if(newHead == None):
            newHead = newNode
            curr = newHead
        else:
            curr.next = newNode
            curr = newNode
        t1 = t1.next
        t2 = t2.next

    while(t1 != None):
        ans = t1.val+carry
        if(ans > 9):
            carry = int(str(ans)[0])
            value = int(str(ans)[1])
        else:
            value = int(str(ans)[0])
            carry = 0
        newNode = ListNode(value)
        if(newHead == None):
            newHead = newNode
            curr = newHead
        else:
            curr.next = newNode
            curr = newNode
        t1 = t1.next

    while(t2 != None):
        ans = t2.val+carry
        if(ans > 9):
            carry = int(str(ans)[0])
            value = int(str(ans)[1])
        else:
            value = int(str(ans)[0])
            carry = 0
        newNode = ListNode(value)
        if(newHead == None):
            newHead-newNode
            curr = newHead
        else:
            curr.next = newNode
            curr = newNode
        t2 = t2.next

    if(carry != 0):
        newNode = ListNode(carry)
        if(newHead == None):
            newHead-newNode
            curr = newHead
        else:
            curr.next = newNode
            curr = newNode
    return newHead
