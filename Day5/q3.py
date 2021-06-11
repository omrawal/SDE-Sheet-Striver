# merge two sorted linked list

# brute force
# create a new linkedlist and
# pointer to each list min to new
# creates LinkedList

# Space O(n+m)
# Time O(n+m)

# optimal
# inplace merge


def optimal(l1, l2):
    if(l1 == None and l2 == None):
        return None
    elif(l1 == None):
        return l2
    elif(l2 == None):
        return l1
    else:
        dummy = None
        current = None
        t1 = l1
        t2 = l2
        while(t1 != None and t2 != None):
            if(t1.val <= t2.val):
                if(current == None):
                    current = t1
                    t1 = t1.next
                    if(dummy == None):
                        dummy = current
                else:
                    current.next = t1
                    current = t1
                    t1 = t1.next
                    if(dummy == None):
                        dummy = current
            else:
                if(current == None):
                    current = t2
                    t2 = t2.next
                    if(dummy == None):
                        dummy = current
                else:
                    current.next = t2
                    current = t2
                    t2 = t2.next
                    if(dummy == None):
                        dummy = current
        while(t1 != None):
            if(current == None):
                current = t1
                t1 = t1.next
                if(dummy == None):
                    dummy = current
            else:
                current.next = t1
                current = t1
                t1 = t1.next
                if(dummy == None):
                    dummy = current
        while(t2 != None):
            if(current == None):
                current = t2
                t2 = t2.next
                if(dummy == None):
                    dummy = current
            else:
                current.next = t2
                current = t2
                t2 = t2.next
                if(dummy == None):
                    dummy = current
        return dummy
