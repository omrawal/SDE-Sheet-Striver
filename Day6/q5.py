# starting point of cycle in linked list

# Brute
# maintain a hash table of all nodes and at first collusion it is the cycle
# else no cycle return null

# Time O(n)
# Space O(n)

# optimal
# Slow and fast pointer method
# when slow and fast collide stop
# entry pointer to head
# move entry and slow one step together till they collide
# the node where they collide is the starting point of cycle


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while(slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next
            if(slow == fast):
                entry = head
                while(entry != slow):
                    slow = slow.next
                    entry = entry.next
                return entry
        return None

# Time O(n)
# Space O(1)
# Intution check in notebook pg27
