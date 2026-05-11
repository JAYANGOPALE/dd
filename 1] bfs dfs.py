'''
dfs algorithm and bfs algorithm , use an unidirected
graph and develop a recursice algorithm for searching all vertices of a graph or tree data structure
'''


from collections import deque

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_iterative(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def build_dynamic_graph():
    graph = {}
    print("--- Dynamic Graph Builder ---")
    try:
        num_edges = int(input("Enter the number of edges: "))
    except ValueError:
        print("Please enter a valid number.")
        return None

    print("Enter each edge as two nodes separated by a space (e.g., A B):")
    for i in range(num_edges):
        while True:
            try:
                u, v = input(f"Edge {i+1}: ").split()
                # Add connection u -> v
                if u not in graph: graph[u] = []
                graph[u].append(v)
                # Add connection v -> u (since it's undirected)
                if v not in graph: graph[v] = []
                graph[v].append(u)
                break
            except ValueError:
                print("Invalid input. Please enter exactly two node names.")
    
    return graph

def main():
    user_graph = build_dynamic_graph()
    if not user_graph:
        return

    start_node = input("\nEnter the starting node for traversal: ")
    
    if start_node not in user_graph:
        print(f"Error: Node '{start_node}' does not exist in the graph.")
        return

    print("\n--- Results ---")
    print("DFS Recursive Traversal:")
    dfs_recursive(user_graph, start_node)
    
    print("\n\nBFS Iterative Traversal:")
    bfs_iterative(user_graph, start_node)
    print("\n")

if __name__ == "__main__":
    main()