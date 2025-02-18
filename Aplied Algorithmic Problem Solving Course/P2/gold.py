"""
Gold - Find the maximum gold that can be safely collected

### How the program solves the problem:
1. Reads the grid and finds the player's starting position ('P').
2. Uses BFS to explore reachable areas while avoiding traps.
3. Stops exploring paths that lead to or are adjacent to traps.
4. Collects gold ('G') along the way.

### Time Complexity:
- O(W * H) where W is width and H is height (BFS visits each cell once).
"""

from collections import deque

def starting_position(w, h, grid):
    """Find the player's start position ('P') in the grid."""
    for x in range(h):
        for y in range(w):
            if grid[x][y] == 'P':
                return x, y  
    return None, None

def is_or_near_trap(x, y, w, h, grid):
    """Check if (x, y) is adjacent to a trap ('T')."""
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # Left, Right, Down, Up

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 'T':
            return True  # If a trap is found nearby, return True

    return False

def get_gold_BFS(w, h, grid):
    """Perform BFS to collect gold safely while avoiding traps."""
    start_x, start_y = starting_position(w, h, grid)
    if start_x is None:  # If 'P' is not found, return 0
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    queue = deque([(start_x, start_y)])  # BFS queue
    visited = set([(start_x, start_y)])  # Track visited positions
    gold_count = 0  

    while queue:
        x, y = queue.popleft()

        # If standing on gold, collect it
        if grid[x][y] == 'G':
            gold_count += 1

        # Stop exploring if near a trap
        if is_or_near_trap(x, y, w, h, grid):
            continue

        # Explore all directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < h and 0 <= ny < w  # Inside bounds
                and grid[nx][ny] != '#'  # Not a wall
                and (nx, ny) not in visited  # Not visited before
            ):
                visited.add((nx, ny))
                queue.append((nx, ny))

    return gold_count

def main():
    """Main function to read input and execute the BFS search."""
    w, h = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]  # Store 2D grid properly

    gold_count = get_gold_BFS(w, h, grid)  # Pass correct arguments

    print(gold_count)  # Print correct result

if __name__ == "__main__":
    main()
