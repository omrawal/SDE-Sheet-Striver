# leetcode problem

def widthOfBinaryTree(self, root) -> int:
    if(root == None):
        return 0
    if(root.left == None and root.right == None):
        return 1
    width = 0
    queue = []
    queue.append((root, 0))
    while(len(queue) > 0):
        currSize = len(queue)
        minVal = queue[0][1]
        firstNode = 0
        lastNode = 0
        for i in range(0, currSize):
            currId = queue[0][1]-minVal
            currNode = queue.pop(0)[0]
            if(i == 0):
                firstNode = currId
            if(i == currSize-1):
                lastNode = currId
            if(currNode.left != None):
                queue.append((currNode.left, currId*2+1))
            if(currNode.right != None):
                queue.append((currNode.right, currId*2+2))
        width = max(width, lastNode-firstNode+1)
    return width
