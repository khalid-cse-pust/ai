import networkx as nx
import matplotlib.pyplot as plt

# Graph input
edges = []

while True:
    e = input("Edge: ")
    if e == "done":
        break
    edges.append(e.split())

G = nx.Graph()
G.add_edges_from(edges)

start = input("Start: ")
goal = input("Goal: ")

# DFS
stack = [start]
visited = set()
parent = {start: None}

while stack:
    node = stack.pop()

    if node in visited:
        continue

    visited.add(node)

    if node == goal:
        break

    for neighbor in G.neighbors(node):
        if neighbor not in visited:
            stack.append(neighbor)
            parent[neighbor] = node

# Find path
if goal in visited:
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    print("Path:", " -> ".join(path))
else:
    print("No path found")

# Draw graph
nx.draw(G, with_labels=True, node_color="lightblue", node_size=800)
plt.show()