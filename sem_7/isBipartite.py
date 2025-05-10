
def bfs(start,colors,graph):
    queue = [start]
    colors[start] = 1
    
    while len(queue)>0:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if colors[neighbor]==0:
                colors[neighbor] = -colors[node]
                queue.append(neighbor)
            elif colors[neighbor] == colors[node]:
               return False
    return True

def isBipartite_bfs(graph):
    n = len(graph)
    colors = [0 for i in range(n)]
    for i in range(n):
        if colors[i]==0:
            if not bfs(i,colors,graph):
                return False
    
    return True

def dfs(node,c,colors,graph):
    colors[node]=c
    for neighbor in graph[node]:
        if colors[neighbor]==0:
            if not dfs(neighbor,-c,colors,graph):
                return False
        elif colors[neighbor]==colors[node]:
            return False
    return True

def isBipartite_dfs(graph):
    n = len(graph)
    colors = [0 for i in range(n)]

    for i in range(n):
        if colors[i]==0:
            if not dfs(i,1,colors,graph):
                return False
    return True




