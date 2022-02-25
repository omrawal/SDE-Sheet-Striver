nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [(1, 2), (2, 3), (3, 5), (5, 7), (2, 7), (4, 6)]


def createAdjacencyList(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    return adjList


def bfs(adjList):
    bfs = []
    visited = [0]*(len(adjList))
    for i in range(1, len(adjList)):
        # if edge is not visited
        if(visited[i] == 0):
            # do the bfs here
            queue = []
            queue.append(i)
            visited[i] = 1
            while(len(queue) > 0):
                edge = queue.pop(0)
                bfs.append(edge)
                for node in adjList[edge]:
                    if(visited[node] == 0):
                        visited[node] = 1
                        queue.append(node)

    return bfs, visited


adjList = createAdjacencyList(nodes=nodes, edges=edges)
print(bfs(adjList=adjList))
