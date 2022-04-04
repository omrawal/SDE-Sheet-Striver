# Kahn's algorithm
# if topological sort cannot be created we say that the graph has a cycle present

from platform import node


nodes = [0, 1, 2, 3, 4, 5]
edges = [(2, 3), (3, 1), (4, 0), (4, 1), (5, 0), (5, 2), ]  # (0, 1), (1, 4)]


def createAdjacencyListDirected(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
    return adjList


def checkCycleBFS(adjList):
    # topoSort = []
    indegree = [0]*len(adjList)
    for i in range(0, len(adjList)-1):
        for j in adjList[i]:
            indegree[j] += 1
    queue = []

    for i in range(0, len(adjList)-1):
        if(indegree[i] == 0):
            queue.append(i)
    count = 0
    while(len(queue) > 0):
        node = queue.pop(0)
        count += 1
        # topoSort.append(node)
        for vertex in adjList[node]:
            indegree[vertex] -= 1
            if(indegree[vertex] == 0):
                queue.append(vertex)
    print('count,len(adjList) = ', count, len(adjList))
    return count == len(adjList)-1


print(checkCycleBFS(createAdjacencyListDirected(nodes, edges)))
