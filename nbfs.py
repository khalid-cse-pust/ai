from collections import deque

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'E', 'G'],
    'C': ['A'],
    'D': ['A'],
    'E': ['B'],
    'G': ['B']
}

def bfs(start, goal):
    q = deque([(start, [start])])
    visited = set([start])

    while q:
        node, path = q.popleft()

        print("Expand:", node, "Queue:", list(q))

        if node == goal:
            return path

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                q.append((child, path + [child]))

print("BFS Path:", bfs('S', 'G'))