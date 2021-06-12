# delete a node
# only node given no head

# better
# copy all values and than point second last to null

# Time O(n) Worst case
# Space O(1)


def better(node):
    temp = node.next
    while(temp.next != None):
        node.val = temp.val
        node = node.next
        temp = temp.next
    node.val = temp.val
    node.next = None

# optimal
# copy the next val to node and point node to next.next
# Time O(1)
# Space O(1)


def optimal(node):
    node.val = node.next.val
    node.next = node.next.next
