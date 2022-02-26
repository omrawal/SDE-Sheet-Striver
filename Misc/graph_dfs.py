# depth first traversal (uses recursion)
nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [(1, 2), (2, 3), (3, 5), (5, 7), (2, 7), (4, 6)]


def createAdjacencyList(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    return adjList


def recDfs(node, visited, adjList, dfsRes):
    dfsRes.append(node)
    visited[node] = 1
    for vertex in adjList[node]:
        if(visited[vertex] == 0):
            recDfs(vertex, visited, adjList, dfsRes)


def recDfsTraversal(adjList):
    dfsRes = []
    visited = [0]*(len(adjList))
    for i in range(1, len(adjList)):
        if(visited[i] == 0):
            recDfs(i, visited, adjList, dfsRes)
    return dfsRes


adjList = createAdjacencyList(nodes=nodes, edges=edges)
print(recDfsTraversal(adjList=adjList))
