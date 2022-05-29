import heapq

base_graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def bfs(graph, start):
    p_queue = list()
    parent = {start: None}
    distance = {start: 0}
    seen = set()
    heapq.heappush(p_queue, (0, start))
    while p_queue:
        pair = heapq.heappop(p_queue)
        seen.add(start)
        dist = pair[0]
        vertex = pair[1]
        for child in graph[vertex].keys():
            if child in seen:
                continue
            if child not in distance or dist + graph[child][vertex] < distance[child]:
                parent[child] = vertex
                heapq.heappush(p_queue, (dist + graph[child][vertex], child))
                distance[child] = dist + graph[child][vertex]
    return parent, distance


if __name__ == '__main__':
    bfs(base_graph, "A")
    parent_res, distance_res = bfs(base_graph, "A")
    print(parent_res)
    print(distance_res)
