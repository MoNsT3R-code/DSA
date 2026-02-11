from collections import deque

def BFS(graph, vertex_start):

    visit = set()
    trans_order = []
    queue = deque([vertex_start])
    visit.add(vertex_start)

    while queue:

        vrtx = queue.popleft()
        trans_order.append(vrtx)
        for nbr in graph[vrtx]:
            if nbr not in visit:
                visit.add(nbr)
                queue.append(nbr)

    return trans_order

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
trans_result = BFS(graph, start_node)
print(trans_result)

