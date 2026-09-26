graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'E', 'G'],
    'C': ['A'],
    'D': ['A'],
    'E': ['B'],
    'G': ['B']
}


def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        print("Expand:", node, "Stack:", [x[0] for x in stack])

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            # Reverse so leftmost child is processed first
            for child in reversed(graph[node]):
                if child not in visited:
                    stack.append((child, path + [child]))

    return None


print("DFS Path:", dfs('S', 'G'))