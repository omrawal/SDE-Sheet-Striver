# Queue using arrays
class MyQueue:

    def __init__(self):
        self.n = 100001
        self.array = [-1 for i in range(self.n)]
        self.left = 0
        self.right = 0
        self.count = 0

    # Function to push an element x in a queue.
    def push(self, x):
        if(self.count < self.n):
            self.array[self.right % self.n] = x
            self.count += 1
            self.right = (self.right+1) % self.n
        else:
            return -1

    # Function to pop an element from queue and return that element.

    def pop(self):
        if(self.count == 0):
            return -1
        else:
            k = self.array[self.left]
            self.array[self.left] = -1
            self.left = (self.left+1) % self.n
            self.count -= 1
            return k

# Time O(1)
# Space O(1)
