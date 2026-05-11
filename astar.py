import heapq

# 1. The Heuristic: Guesses the distance from the current square to the goal
def heuristic(a, b):
    # Manhattan distance: simply counting grid steps (no diagonals)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_simple(grid, start, goal):
    # The 'open_set' acts as our checklist of squares to explore next.
    # It stores tuples: (f_score, (x, y))
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # 'came_from' acts like breadcrumbs so we can walk back and draw the path
    came_from = {}
    
    # 'g_score' is the exact cost it took to get from the start to this square
    g_score = {start: 0}
    
    rows = len(grid)
    cols = len(grid[0])
    
    while open_set:
        # 2. Always pick the square with the lowest estimated total cost
        current_f, current = heapq.heappop(open_set)
        
        # 3. If we reached the goal, follow the breadcrumbs backwards!
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] # Reverse the list to go from start -> goal
        
        # 4. Check the 4 neighboring squares (Up, Down, Left, Right)
        x, y = current
        neighbors = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
        
        for neighbor in neighbors:
            nx, ny = neighbor
            
            # Make sure we don't step off the map, and we don't walk into a wall (1)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                
                # The cost to move to the next square is just 1 step
                new_cost = g_score[current] + 1
                
                # If we've never been to this neighbor, or we found a shorter route to it...
                # (float('inf') just means 'infinity', representing an unvisited square)
                if new_cost < g_score.get(neighbor, float('inf')):
                    
                    # Update our records!
                    came_from[neighbor] = current
                    g_score[neighbor] = new_cost
                    
                    # f_score = steps taken so far + guessed steps remaining
                    f_score = new_cost + heuristic(neighbor, goal)
                    
                    # Add this neighbor to our checklist to explore later
                    heapq.heappush(open_set, (f_score, neighbor))
                    
    # If the checklist empties and we never hit the goal, there's no path.
    return None

# --- Example Usage ---
grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
path = a_star_simple(grid, (0,0), (3,3))
print("Path:", path)