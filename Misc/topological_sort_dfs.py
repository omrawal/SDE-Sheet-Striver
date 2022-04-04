# DAG directed acyclic graph needed
# Linear ordering of vertices such that if there is an edge u -> v
# u appears before v in that ordering
# there can be multiple answers (Topological sorts)

nodes = [0, 1, 2, 3, 4, 5]
edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]


def createAdjacencyListDirected(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
    return adjList


def topoDFS(node, adjList, visited, stack):
    visited[node] = 1
    for vertex in adjList[node]:
        if(visited[vertex] == 0):
            topoDFS(vertex, adjList, visited, stack)
    stack.append(node)


def getTopologicalSort(adjList):
    visited = [0]*len(adjList)
    stack = []
    for i in range(0, len(adjList)-1):
        if(visited[i] == 0):
            topoDFS(i, adjList, visited, stack)
    topoSort = []
    while(len(stack) > 0):
        topoSort.append(stack.pop(-1))
    return topoSort


print(getTopologicalSort(createAdjacencyListDirected(nodes, edges)))
