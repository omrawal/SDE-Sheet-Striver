# intersection of 2 linkedlist


# Brute

# iterate first list;
# for every node in first iterate second on entirely

# Time O(n*m)
# Space O(1)


# Better

# iterate throught first list;
# for every node hash its address in hash table
# iterate through second list
# for each node check if its address is present in hash table
# if present return that node

# Time O(n+m)
# space O(n)


# Optimal 1

# n<m
# find length of both simultaneously in O(m)
# take two pointers
# move pointer to smaller list by m-n steps
# move both pointers simultaneously and check if they are pointing to same node
# if yes return any one node
# at end if not found intersection both will poit null return null

# Time O(m) for length + O(m-n) difference traversal by longer LL + O(n) remaining traversal
# Space O(1)

# Optimal 2

# set pointers to head of each linkedlists
# move both simulatanously when one becomes null make take point to head of other
# continue moving when other becomes null make it head of first
# now move both simultaneously if they point to same node return the node
# else they point null if no intersection

# Overall has same time and space complexity as optimal 1 but faster to code

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def optimal2(self, headA: ListNode, headB: ListNode) -> ListNode:
    t1 = headA
    t2 = headB
    while(t1 != None and t2 != None):
        t1 = t1.next
        t2 = t2.next
    if(t1 == None):
        t1 = headB
    elif(t2 == None):
        t2 = headA

    while(t1 != None and t2 != None):
        t1 = t1.next
        t2 = t2.next
    if(t1 == None):
        t1 = headB
    elif(t2 == None):
        t2 = headA

    while(t1 != None and t2 != None):
        if(t1 == t2):
            return t1
        t1 = t1.next
        t2 = t2.next
    return None
