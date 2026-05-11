# ==========================================
# HELPER: Find Smallest Item in a List
# ==========================================
def pop_smallest(my_list):
    min_index = 0
    for i in range(len(my_list)):
        if my_list[i][0] < my_list[min_index][0]:
            min_index = i
    return my_list.pop(min_index)

# ==========================================
# 1. A* SEARCH ALGORITHM
# ==========================================
def a_star_search(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    rows, cols = len(grid), len(grid[0])
    
    while open_set:
        current_f, current = pop_smallest(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] 
        
        x, y = current
        for nx, ny in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_score[current] + 1
                if new_cost < g_score.get((nx, ny), float('inf')):
                    came_from[(nx, ny)] = current
                    g_score[(nx, ny)] = new_cost
                    f_score = new_cost + heuristic((nx, ny), goal)
                    open_set.append((f_score, (nx, ny)))
    return None

# ==========================================
# 2. SELECTION SORT
# ==========================================
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# ==========================================
# 3. PRIM'S ALGORITHM
# ==========================================
def prims_mst(graph, start_node):
    mst = []
    visited = set([start_node])
    edges = []
    
    for neighbor, weight in graph[start_node]:
        edges.append((weight, start_node, neighbor))
        
    while edges:
        weight, frm, to = pop_smallest(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for next_neighbor, next_weight in graph[to]:
                if next_neighbor not in visited:
                    edges.append((next_weight, to, next_neighbor))
    return mst

# ==========================================
# 4. KRUSKAL'S ALGORITHM
# ==========================================
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    def find(self, item):
        if self.parent[item] == item: return item
        return self.find(self.parent[item])
    def union(self, set1, set2):
        self.parent[self.find(set1)] = self.find(set2)

def kruskals_mst(vertices, edges):
    mst = []
    edges.sort(key=lambda x: x[2]) 
    ds = DisjointSet(vertices)
    
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
    return mst

# ==========================================
# 5. DIJKSTRA'S ALGORITHM
# ==========================================
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = pop_smallest(queue)
        if current_distance > distances[current_node]: continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((distance, neighbor))
    return distances

# ==========================================
# 6. JOB SCHEDULING
# ==========================================
def job_scheduling(jobs, max_deadline):
    jobs.sort(key=lambda x: x[2], reverse=True)
    slots = [False] * max_deadline
    schedule = ['-'] * max_deadline
    total_profit = 0
    
    for job_id, deadline, profit in jobs:
        for j in range(min(max_deadline - 1, deadline - 1), -1, -1):
            if not slots[j]:
                slots[j] = True
                schedule[j] = job_id
                total_profit += profit
                break
    return schedule, total_profit


# ==========================================
# DYNAMIC MENU INTERFACE
# ==========================================
def main_menu():
    # Pre-defined graphs to save you from typing complex dictionaries manually
    sample_graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1)],
        'C': [('A', 3), ('B', 1), ('D', 4)],
        'D': [('B', 1), ('C', 4)]
    }
    
    while True:
        print("\n" + "="*30)
        print(" GREEDY ALGORITHM VISUALIZER ")
        print("="*30)
        print("1. A* Search (Pathfinding)")
        print("2. Selection Sort")
        print("3. Prim's Minimum Spanning Tree")
        print("4. Kruskal's Minimum Spanning Tree")
        print("5. Dijkstra's Shortest Path")
        print("6. Job Scheduling")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            print("\n--- A* Search ---")
            print("Using a 3x3 grid with a wall in the middle.")
            grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            start_x = int(input("Enter start X coordinate (0-2): "))
            start_y = int(input("Enter start Y coordinate (0-2): "))
            goal_x = int(input("Enter goal X coordinate (0-2): "))
            goal_y = int(input("Enter goal Y coordinate (0-2): "))
            path = a_star_search(grid, (start_x, start_y), (goal_x, goal_y))
            print(f"Resulting Path: {path}")

        elif choice == '2':
            print("\n--- Selection Sort ---")
            user_input = input("Enter numbers separated by commas (e.g., 5,2,9,1): ")
            # Convert user input string into a list of integers
            arr = [int(x.strip()) for x in user_input.split(',')]
            print(f"Original Array: {arr}")
            print(f"Sorted Array:   {selection_sort(arr)}")

        elif choice == '3':
            print("\n--- Prim's Algorithm ---")
            print(f"Available Nodes: {list(sample_graph.keys())}")
            start_node = input("Enter starting node (A, B, C, or D): ").upper()
            if start_node in sample_graph:
                print(f"Prim's MST from {start_node}: {prims_mst(sample_graph, start_node)}")
            else:
                print("Invalid node!")

        elif choice == '4':
            print("\n--- Kruskal's Algorithm ---")
            verts = ['A', 'B', 'C', 'D']
            edges_list = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 1), ('C', 'D', 4)]
            print("Using pre-defined edges for A, B, C, D.")
            print(f"Kruskal's MST: {kruskals_mst(verts, edges_list)}")

        elif choice == '5':
            print("\n--- Dijkstra's Algorithm ---")
            print(f"Available Nodes: {list(sample_graph.keys())}")
            start_node = input("Enter starting node (A, B, C, or D): ").upper()
            if start_node in sample_graph:
                print(f"Shortest distances from {start_node}: {dijkstra(sample_graph, start_node)}")
            else:
                print("Invalid node!")

        elif choice == '6':
            print("\n--- Job Scheduling ---")
            print("Using sample jobs: J1(Profit 100, D:2), J2(Profit 19, D:1), J3(Profit 27, D:2)")
            jobs_list = [['J1', 2, 100], ['J2', 1, 19], ['J3', 2, 27]]
            max_d = int(input("Enter maximum deadline to consider (e.g., 2 or 3): "))
            sched, prof = job_scheduling(jobs_list, max_d)
            print(f"Optimal Schedule: {sched} | Total Profit: {prof}")

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please pick a number from 1 to 7.")

# Run the dynamic menu when the script starts
if __name__ == "__main__":
    main_menu()