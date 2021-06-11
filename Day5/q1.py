# Reverse a linked list

# brute
# iterate ans create a new array O(n) time O(n) space
# create a new linked list O(N)
# fill the values in reverse order of array
# Time O(N+N)
# SpaceO(N+N)

# Optimal
# Time O(n)
# Space O(1)


def optimal(head):
    if(head == None):
        return head
    else:
        dummy = None
        while(head != None):
            next = head.next
            head.next = dummy
            dummy = head
            head = next
        return dummy
