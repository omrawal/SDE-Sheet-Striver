# cant use undirected logic as the two different paths may reach the same node
# that might be considered as cycle
# Hence we need 2 arrays one visited, one DfsVis

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
edges = [(1, 2), (2, 3), (3, 4), (3, 6), (4, 5),
         (6, 5), (7, 2), (7, 8), (8, 9), (9, 7)]


def createAdjacencyListDirected(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
    return adjList


def detectCycleDFS(node, adjList, visited, dfsVis):
    visited[node] = 1
    dfsVis[node] = 1
    for vertex in adjList[node]:
        if(visited[vertex] == 0):
            if(detectCycleDFS(vertex, adjList, visited, dfsVis)):
                return True
        elif(visited[vertex] == 1 and dfsVis[vertex] == 1):
            return True
    dfsVis[node] = 0
    return False
    # pass


def isCycle(adjList):
    visited = [0]*len(adjList)
    dfsVis = [0]*len(adjList)
    for i in range(1, len(adjList)):
        if(detectCycleDFS(i, adjList, visited, dfsVis)):
            return True
    return False


print(isCycle(createAdjacencyListDirected(nodes, edges)))
