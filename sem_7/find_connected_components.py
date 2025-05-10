
def dfs(graph,v,visited,component):
    visited[v] = True
    component.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited,component)



def find_connected_componenets(graph):
    visited = {node: False for node in graph}

    connected_components = []

    for cur_Node in graph:
        if not visited[cur_Node]:
            component = []
            dfs(graph,cur_Node,visited,component)
            connected_components.append(component)
    return connected_components

def dfs_color(graph,v,visited,color):
    visited[v] = color
    for i in graph[v]:
        if visited[i]==0:
            dfs_color(graph,i,visited,color)


def find_connected_components_color(graph):
    visited = {node:0 for node in graph}

    color = 0
    for cur_Node in graph:
        if not visited[cur_Node]:
            color+=1
            dfs_color(graph,cur_Node,visited,color)

    return visited
