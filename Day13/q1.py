# stack using arrays
class MyStack:

    def __init__(self):
        self.arr = [None for i in range(100)]
        self.pointer = -1
    # Function to push an integer into the stack.

    def push(self, data):
        # add code here
        self.arr[self.pointer+1] = data
        self.pointer += 1

    # Function to remove an item from top of the stack.
    def pop(self):
        # add code here
        if(self.pointer == -1):
            return self.pointer
        else:
            k = self.arr[self.pointer]
            self.pointer -= 1
            return k

# Time O(1)
# Space O(1) push and pop ops
