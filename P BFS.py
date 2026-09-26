import networkx as nx              # For creating and handling graphs
import matplotlib.pyplot as plt    # For drawing the graph
from collections import deque      # For implementing the BFS queue

edges = []                                             # Empty list to store all edges
print("Enter edges (e.g., A B). Type 'done' when finished:")

while True:                                            # Keep taking input until user types 'done'
    e = input()                                        # Read one edge from the user
    if e.lower() == 'done':                            # If user types 'done', stop taking input
        break 
    a, b = e.split()                                   # Split input into two nodes (e.g., "A B" → a='A', b='B')
    edges.append((a, b))                               # Add the edge as a tuple (a, b) to the list

G = nx.Graph()                                         # Create an empty undirected graph object
G.add_edges_from(edges)                                # Add all user-entered edges to the graph

start = input("Enter start node: ").strip()            # Input the node where BFS will start
goal = input("Enter goal node: ").strip()              # Input the node we are searching for

visited = set()                                        # To store all visited nodes and avoid revisits
queue = deque([[start]])                               # Initialize queue with the start node path as a list
found_path = None                                       # Variable to store the final path when found

while queue:                                           # Continue until queue becomes empty
    path = queue.popleft()                             # Remove the first path from the queue (FIFO)
    node = path[-1]                                    # Get the last node from the current path

    if node == goal:                                   # If the goal node is reached
        found_path = path                              # Save this path as the found path
        break                                          # Stop the search since BFS guarantees shortest path

    if node not in visited:                            # If the node has not been explored yet
        for neighbor in G.neighbors(node):             # Loop through all its connected neighbors
            new_path = list(path)                      # Copy the current path
            new_path.append(neighbor)                  # Add the neighbor to the new path
            queue.append(new_path)                     # Enqueue the new extended path
        visited.add(node)                              # Mark the node as visited so it won't be expanded again

if found_path:                                         # If a path was found
    print("Path found:", " -> ".join(found_path))      # Print the nodes in the path with arrows
else:
    print("No path found.")                            # If queue became empty without finding goal

pos = nx.spring_layout(G)                              # Compute positions for nodes (for visualization)
nx.draw(G, pos, with_labels=True,                      # Draw the full graph
        node_color='lightblue', node_size=800,
        font_size=10, width=2)

if found_path:  
    path_edges = list(zip(found_path, found_path[1:])) # Pair up consecutive nodes to get path edges
    nx.draw_networkx_nodes(G, pos,                     # Highlight the path nodes in orange
                           nodelist=found_path, 
                           node_color='orange', 
                           node_size=900)
    nx.draw_networkx_edges(G, pos,                     # Highlight the path edges in red
                           edgelist=path_edges, 
                           edge_color='red', width=3)

plt.title("BFS Traversal and Found Path")              # Set title for the plot
plt.show()                                             # Display the graph on screen
