# bipartite when we color nodes using 2 colors and no two adjacent nodes have the same color
# when the is no odd length cycle (even length or no cycle allowed)

# GIVES RUNTIME ERROR OF GFG


# odd length cycle present # is NOT bipartite
nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [(1, 2), (2, 3), (2, 8), (3, 4), (8, 5),
         (4, 5), (5, 6), (6, 7), ]

# odd length cycle absent (even length cycle) # is bipartite
nodes = [1, 2, 3, 4, 5, 6, 7, 8]
edges = [(1, 2), (2, 3), (2, 7), (3, 4), (4, 5),
         (5, 8), (7, 6), (6, 5), ]


def createAdjacencyList(nodes, edges):
    adjList = [[]for i in range(len(nodes)+1)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    return adjList


def dfsBipartite(node, adjList, color):
    for vertex in adjList[node]:
        if(color[vertex] == -1):
            if(color[node] == 0):
                color[vertex] = 1
            else:
                color[vertex] = 0
            if(not dfsBipartite(vertex, adjList, color)):
                return False
        elif(color[vertex] == color[node]):
            return False
    return True


def checkBipartite(adjList):
    color = [-1]*len(adjList)
    for i in range(1, len(adjList)):
        if(color[i] == -1):
            if(not dfsBipartite(i, adjList, color)):
                return False
    return True


adjList = createAdjacencyList(nodes=nodes, edges=edges)
print(checkBipartite(adjList=adjList))
