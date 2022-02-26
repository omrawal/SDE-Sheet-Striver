# intuition is when you traverse and find a visited node it means there exists a cycle
# when calling recursive function pass a parent along with a node
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
edges = [(1, 2), (2, 4), (3, 5), (5, 6), (5, 10),
         (6, 7), (7, 8), (10, 9), (9, 8), (8, 11)]


def createAdjacencyList(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    return adjList


def isCycleDFS(node, adjList, visited, parent):
    visited[node] = 1
    for vertex in adjList[node]:
        if(visited[vertex] == 0):
            if(isCycleDFS(vertex, adjList, visited, node)):
                return True
        elif(vertex != parent and parent != -1):
            return True
    return False


def isCycle(adjList):
    visited = [0]*(len(adjList))
    for i in range(1, len(adjList)):
        if(visited[i] == 0):
            if(isCycleDFS(i, adjList, visited, parent=-1)):
                return True
    return False


adjList = createAdjacencyList(nodes=nodes, edges=edges)
print(isCycle(adjList=adjList))
