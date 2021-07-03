# Stack using queues
# we use 2 queues for this method

# algo

# -> push
# add n to q2
# q1 to q2 element by element
# swap q1,q2

# -> pop
# return  top of q1

import copy


class Queue(object):
    def __init__(self) -> None:
        self.qlist = []

    def push(self, val):
        self.qlist.append(val)
        return True

    def pop(self):
        k = self.qlist.pop(0)
        return k


def swap(obj1, obj2):
    k = copy.deepcopy(obj1)
    obj1 = copy.deepcopy(obj2)
    obj2 = copy.deepcopy(k)
    return obj1, obj2


class Stackq(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def pop(self):
        if(len(self.q1.qlist) < 1):
            return None
        else:
            return self.q1.pop()

    def push(self, val):
        self.q2.push(val)
        while(len(self.q1.qlist) > 0):
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = swap(self.q1, self.q2)
        return True


sq = Stackq()
print('pushing 1')
sq.push(1)
print('popping')
print(sq.pop())
print('pushing 2')
sq.push(2)
print('pushing 3')
sq.push(3)
print('pushing 4')
sq.push(4)
print('popping')
print(sq.pop())
print('pushing 5')
sq.push(5)
print('popping')
print(sq.pop())
print('popping')
print(sq.pop())
print('popping')
print(sq.pop())
