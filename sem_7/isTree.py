

def isTree(graph,start):
    visited = []
    queue = [start]
    parent = {start:None}

    while queue:
        v = queue.pop()
        visited.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = v
            else:
                if parent[v]!=neighbor:
                    return False
    
    return len(visited)==len(graph)