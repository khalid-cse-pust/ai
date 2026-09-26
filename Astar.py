import networkx as nx
import matplotlib.pyplot as plt
import heapq

# --- Input graph edges ---
edges = []
print("Enter edges (e.g., A B cost). Type 'done' when finished:")
while True:
    e = input()
    if e.lower() == 'done':
        break
    a, b, c = e.split()
    edges.append((a, b, float(c)))

# Create undirected weighted graph
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

# --- Start and goal nodes ---
start = input("\nEnter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

# --- A* Search Implementation ---
open_list = []
heapq.heappush(open_list, (heuristic.get(start, float('inf')), [start]))  # f = g + h, here g=0 at start
g_cost = {start: 0}
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
            cost = g_cost[node] + G[node][neighbor]['weight']
            if cost < g_cost.get(neighbor, float('inf')):  # found a better path
                g_cost[neighbor] = cost
                f_val = cost + heuristic.get(neighbor, float('inf'))  # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (f_val, path + [neighbor]))

# --- Compute total cost of found path ---
if found_path:
    total_cost = sum(G[found_path[i]][found_path[i + 1]]['weight'] for i in range(len(found_path) - 1))
    print("\nPath found (A*):", " -> ".join(found_path))
    print("Total path cost (g):", total_cost)
else:
    print("\nNo path found.")
    total_cost = None

# --- Draw the graph ---
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10)
nx.draw_networkx_edges(G, pos, width=2)

# --- Edge weight labels ---
for (u, v), w in edge_labels.items():
    x_mid = (pos[u][0] + pos[v][0]) / 2
    y_mid = (pos[u][1] + pos[v][1]) / 2
    plt.text(x_mid, y_mid + 0.04, str(w), fontsize=9,
             horizontalalignment='center', verticalalignment='center',
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

# --- Highlight found path ---
if found_path:
    path_edges = list(zip(found_path, found_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=found_path, node_color='orange', node_size=900)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

# --- Show (g,h,f) for every node ---
for n in G.nodes():
    g_val = g_cost.get(n, float('inf'))
    h_val = heuristic.get(n, float('inf'))
    f_val = g_val + h_val if g_val != float('inf') and h_val != float('inf') else float('inf')

    g_text = "∞" if g_val == float('inf') else f"{g_val}"
    h_text = "∞" if h_val == float('inf') else f"{h_val}"
    f_text = "∞" if f_val == float('inf') else f"{f_val}"

    x, y = pos[n]
    plt.text(x, y - 0.08, f"g={g_text}, h={h_text}, f={f_text}", fontsize=9,
             horizontalalignment='center',
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

plt.title("A* Search (f = g + h)")
plt.axis('off')
plt.show()
