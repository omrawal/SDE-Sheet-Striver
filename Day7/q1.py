# Clone linkedlist with next and random pointer

# Brute
# using Hashmap


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# incorrect output


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hashset = {}
        t = head
        while(t != None):
            hashset[t] = Node(t.val)
            t = t.next

        t = head
        while(t != None):
            hashset[t].next = hashset.get(t.next)
            hashset[t].random = hashset.get(t.random)
            t = t.next
        # newhead = hashset[head]

        return hashset.get(head)

# Time = O(n)+O(n)=O(2n)=O(n)
# Space = O(n)

# Optimal
#
# Create copy node and insert right after the original one
# now solving the problem of random pointer now its just the next of destination pointer
# resetting the pointers and separating the list
