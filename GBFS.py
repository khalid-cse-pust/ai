import networkx as nx
import matplotlib.pyplot as plt
import heapq

# --- Input graph edges ---
edges = []
print("Enter edges (e.g., A B cost). Type 'done' when finished:")
while True:
    e = input()
    if e.lower() == "done":
        break
    a, b, c = e.split()
    edges.append((a, b, float(c)))  # cost is used for display

G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# --- Take heuristic values ---
heuristic = {}
print("\nEnter heuristic values (e.g., A 6). Type 'done' when finished:")
while True:
    h = input()
    if h.lower() == 'done':
        break
    n, val = h.split()
    heuristic[n] = float(val)

# --- Take start and goal ---
start = input("\nEnter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

# --- Greedy Best First Search ---
open_list = []
heapq.heappush(open_list, (heuristic.get(start, float('inf')), [start]))
visited = set()
found_path = None

while open_list:
    f, path = heapq.heappop(open_list)
    node = path[-1]
    if node == goal:
        found_path = path
        break
    if node not in visited:
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(open_list, (heuristic.get(neighbor, float('inf')), new_path))

# --- Print result ---
if found_path:
    print("\nPath found (Greedy Best First Search):", " -> ".join(found_path))
else:
    print("\nNo path found.")

# --- Draw graph and highlight the path ---
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')  # {(u,v): weight, ...}

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10)
nx.draw_networkx_edges(G, pos, width=2)

# --- Draw edge labels manually at midpoints, shifted upward so they don't get hidden by the red path ---
for (u, v), w in labels.items():
    x_mid = (pos[u][0] + pos[v][0]) / 2
    y_mid = (pos[u][1] + pos[v][1]) / 2
    # shift upward; tune the offset (0.03) if you need more/less separation
    plt.text(x_mid, y_mid + 0.03, str(w), fontsize=9,
             horizontalalignment='center', verticalalignment='center',
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

if found_path:
    path_edges = list(zip(found_path, found_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=found_path, node_color='orange', node_size=900)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title("Greedy Best First Search (f(n) = h(n)) with g(n) Above Edges")
plt.axis('off')
plt.show()
