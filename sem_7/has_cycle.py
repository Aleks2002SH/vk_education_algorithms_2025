def dfs(graph,v,parent,visited):
    visited.append(v)
    for neighbor in graph[v]:
        if neighbor!=parent:
            if neighbor in visited or dfs(graph,neighbor,v,visited):
                return True
    return False


def has_cycle(graph):
    visited = []
    for v in graph:
        if v not in visited:
            if dfs(graph,v,None,visited):
                return True 
    return False