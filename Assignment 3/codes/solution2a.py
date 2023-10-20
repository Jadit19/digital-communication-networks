import sys

# Define the graph and weights
graph = {(0, 1): 1, (0, 2): 3, (0, 3): 7, (1, 2): 1, (2, 3): 2}


# Function to find the node with the minimum distance value
def min_distance(distances, visited):
    min_dist = sys.maxsize
    min_node = None
    for node in range(len(distances)):
        if distances[node] < min_dist and not visited[node]:
            min_dist = distances[node]
            min_node = node
    return min_node


# Function to print the routing table
def print_routing_table(node, distances, previous_nodes):
    print("=" * 30)
    print(f"Node {node} Routing Table:")
    print("-" * 30)
    print("Destination | Cost | Next Hop")
    print("-" * 30)
    for i in range(len(distances)):
        if i != node:
            path = []
            curr_node = i
            while curr_node is not None:
                path.insert(0, curr_node)
                curr_node = previous_nodes[curr_node]
            print(
                f"{i}           | {distances[i]}    | {path[1] if len(path) > 1 else '-'}"
            )
    print("=" * 30 + "\n")


# Dijkstra's algorithm
def dijkstra(graph, start_node):
    num_nodes = len(set(sum(graph.keys(), ())))

    distances = [sys.maxsize] * num_nodes
    previous_nodes = [None] * num_nodes
    visited = [False] * num_nodes

    distances[start_node] = 0

    for _ in range(num_nodes):
        current_node = min_distance(distances, visited)
        visited[current_node] = True

        for edge, weight in graph.items():
            if current_node in edge:
                neighbor = edge[0] if edge[1] == current_node else edge[1]
                if (
                    not visited[neighbor]
                    and distances[neighbor] > distances[current_node] + weight
                ):
                    distances[neighbor] = distances[current_node] + weight
                    previous_nodes[neighbor] = current_node

    return distances, previous_nodes


# Run Dijkstra's algorithm for each node
for node in range(4):
    distances, previous_nodes = dijkstra(graph, node)
    print_routing_table(node, distances, previous_nodes)
