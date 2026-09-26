import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Graph input
edges = []

print("Enter edges (A B). Type done to finish:")

while True:
    x = input()

    if x == "done":
        break

    a, b = x.split()
    edges.append((a, b))

# Create graph
G = nx.Graph()
G.add_edges_from(edges)

# Start and Goal
start = input("Start: ")
goal = input("Goal: ")

# BFS
queue = deque([[start]])
visited = {start}
path = None

while queue:

    current_path = queue.popleft()
    node = current_path[-1]

    # Goal found
    if node == goal:
        path = current_path
        break

    # Visit neighbors
    for neighbor in G.neighbors(node):

        if neighbor not in visited:
            visited.add(neighbor)

            new_path = current_path + [neighbor]
            queue.append(new_path)

# Result
if path:
    print("Path:", " -> ".join(path))
else:
    print("No path found")

# Draw graph
pos = nx.spring_layout(G)

nx.draw(
    G, pos,
    with_labels=True,
    node_color="lightblue",
    node_size=800
)

# Highlight BFS path
if path:
    path_edges = list(zip(path, path[1:]))

    nx.draw_networkx_nodes(
        G, pos,
        nodelist=path,
        node_color="orange"
    )

    nx.draw_networkx_edges(
        G, pos,
        edgelist=path_edges,
        edge_color="red",
        width=3
    )

plt.title("BFS Shortest Path")
plt.show()