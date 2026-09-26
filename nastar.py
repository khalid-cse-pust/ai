import heapq

graph = {
    'S': [('A', 2), ('B', 1)],
    'A': [('S', 2), ('C', 2)],
    'B': [('S', 1), ('D', 4)],
    'C': [('A', 2), ('G', 3)],
    'D': [('B', 4), ('G', 1)],
    'G': [('C', 3), ('D', 1)]
}

# Heuristic values
h = {
    'S': 5,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 1,
    'G': 0
}


def a_star(start, goal):

    # Priority queue: (f, g, node, path)
    pq = [(h[start], 0, start, [start])]

    # Best known g-cost for each node
    best_g = {start: 0}

    while pq:

        # Get node with smallest f value
        f, g, node, path = heapq.heappop(pq)

        print(
            "Expand:",
            node,
            "g =",
            g,
            "h =",
            h[node],
            "f =",
            f
        )

        # Goal found
        if node == goal:
            return path, g

        # Skip outdated/worse path
        if g != best_g.get(node, float("inf")):
            continue

        # Explore neighbors
        for child, cost in graph[node]:

            new_g = g + cost

            # If this is a better path
            if new_g < best_g.get(child, float("inf")):

                best_g[child] = new_g

                new_f = new_g + h[child]

                heapq.heappush(
                    pq,
                    (new_f, new_g, child, path + [child])
                )


print(a_star('S', 'G'))