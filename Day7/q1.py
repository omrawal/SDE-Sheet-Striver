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
            hashset[t].next = hashset[t.next]
            hashset[t].random = hashset[t.random]
            t = t.next
        newhead = hashset[head]

        return newhead
