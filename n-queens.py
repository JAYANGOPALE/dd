def solve_n_queens(n):
    """
    Solves the N-Queens problem using Backtracking and Branch & Bound.
    Returns a list of all valid board configurations.
    """
    board = [[0] * n for _ in range(n)]
    all_solutions = []

    # BRANCH AND BOUND ARRAYS
    # These act as our bounds, immediately telling us if a branch is invalid in O(1) time.
    cols_under_attack = [False] * n
    
    # A board has 2*N - 1 diagonals in each direction.
    # Left diagonals ( \ ): The difference (row - col) is constant for elements on the same diagonal.
    left_diagonals = [False] * (2 * n - 1)
    
    # Right diagonals ( / ): The sum (row + col) is constant for elements on the same diagonal.
    right_diagonals = [False] * (2 * n - 1)

    def backtrack(row):
        # Base case: If we successfully placed a queen in every row, we found a solution.
        if row == n:
            solution = []
            for r in range(n):
                # Convert the row into a readable string (Q for Queen, . for empty)
                row_string = "".join(["Q " if board[r][c] == 1 else ". " for c in range(n)])
                solution.append(row_string)
            all_solutions.append(solution)
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            # Calculate the unique index for this cell's left and right diagonals
            ld_idx = row - col + (n - 1) # Add (n-1) to avoid negative indices
            rd_idx = row + col

            # BRANCH AND BOUND: Check our constraints. 
            # If the column or either diagonal is under attack, prune this branch.
            if not cols_under_attack[col] and not left_diagonals[ld_idx] and not right_diagonals[rd_idx]:
                
                # 1. PLACE THE QUEEN
                board[row][col] = 1
                cols_under_attack[col] = True
                left_diagonals[ld_idx] = True
                right_diagonals[rd_idx] = True

                # 2. RECURSE to the next row
                backtrack(row + 1)

                # 3. BACKTRACK: Remove the queen and lift the constraints
                board[row][col] = 0
                cols_under_attack[col] = False
                left_diagonals[ld_idx] = False
                right_diagonals[rd_idx] = False

    # Start the backtracking process from the 0th row
    backtrack(0)
    return all_solutions

# --- Example Usage ---
if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    
    print(f"Found {len(solutions)} solutions for {n}-Queens:\n")
    for idx, sol in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in sol:
            print(row)
        print("-" * (n * 2))