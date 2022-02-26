# intuition is when you traverse and find a visited node it means there exists a cycle
# when pushing node in queue < node, parent >
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
edges = [(1, 2), (2, 4), (3, 5), (5, 6), (5, 10),
         (6, 7), (7, 8), (10, 9), (9, 8), (8, 11)]


def createAdjacencyList(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    return adjList


def checkCycle(node, adjList, visited):
    queue = []
    visited[node] = 1
    queue.append((node, -1))
    while(len(queue) > 0):
        currNode = queue.pop(0)
        currVertex = currNode[0]
        currParent = currNode[1]
        for vertex in adjList[currVertex]:
            if(visited[vertex] == 0):
                visited[vertex] = 1
                queue.append((vertex, currVertex))
            elif(vertex != currParent and currParent != -1):
                return True
    return False


def isCycle(adjList):
    visited = [0]*(len(adjList))
    for i in range(1, len(adjList)):
        if(checkCycle(i, adjList, visited)):
            return True
    return False


adjList = createAdjacencyList(nodes=nodes, edges=edges)
print(isCycle(adjList=adjList))
