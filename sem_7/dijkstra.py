import heapq

def dijkstra(graph,start):
    distances = {v:float('infinity') for v in graph}
    distances[start] = 0
    priority_queue = [(0,start)]
    while priority_queue:
        cur_dist,cur_v = heapq.heappop(priority_queue)
        if cur_dist > distances[cur_v]:
            continue
        
        for neighbor, weight in graph[cur_v].items():
            dist = cur_dist + weight

            if dist<distances[neighbor]:
                distances[neighbor]=dist
                heapq.heappush(priority_queue,(dist,neighbor))
        
    return distances