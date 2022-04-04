# DAG directed acyclic graph needed
# Linear ordering of vertices such that if there is an edge u -> v
# u appears before v in that ordering
# there can be multiple answers (Topological sorts)

# Kahn's algorithm


nodes = [0, 1, 2, 3, 4, 5]
edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2)]


def createAdjacencyListDirected(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
    return adjList


def topoSortBFS(adjList):
    topoSort = []
    indegree = [0]*len(adjList)
    for i in range(0, len(adjList)-1):
        for j in adjList[i]:
            indegree[j] += 1
    queue = []
    for i in range(0, len(adjList)-1):
        if(indegree[i] == 0):
            queue.append(i)
    while(len(queue) > 0):
        node = queue.pop(0)
        topoSort.append(node)
        for vertex in adjList[node]:
            indegree[vertex] -= 1
            if(indegree[vertex] == 0):
                queue.append(vertex)
    return topoSort


print(topoSortBFS(createAdjacencyListDirected(nodes, edges)))
