"""
* Robot Tour Optimization – Nearest Neighbor Heuristic *

This program implements a heuristic solution to the problem where a robotic arm must visit a series of 
points on a circuit board in an optimized order. The problem is a variation of the classic 
"Traveling Salesman Problem (TSP)," where we aim to find the shortest cyclic tour that visits each 
point exactly once.

* Solution Approach: *
1. Reading Input from Standard Input (sys.stdin)
   - The program expects a list of points in the plane where:
     - Lines starting with `#` are ignored as comments.
     - The first relevant line specifies the number of points.
     - The following lines contain `(x, y)` coordinates as integer values.
     ```

2. Implementing the Nearest-Neighbor Heuristic
   - The algorithm selects a starting point (the first point in the input list).
   - It iteratively selects the nearest unvisited point and adds it to the tour.
   - The process repeats until all points are visited.
   - Finally, it returns to the starting point to complete the cycle.

3. Calculating Distances:
   - The program computes the Euclidean distance between two points `(x1, y1)` and `(x2, y2)`:
     ```
     d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
     ```
   - This helps determine which point is closest at each step.

4. Generating the Output
   - The computed tour is printed in the required format:
     - First line: The number of points.
     - Following lines: `(x, y)` coordinates in visit order.

"""

import sys
import math

def read_tsp_stdin():
    """
    Reads input from standard input and returns a list of points (x, y).
    Ignores comment lines starting with '#' and skips empty lines.
    """
    points = []
    num_points = None  # Track the number of points

    for line in sys.stdin:
        line = line.strip()  # Remove leading/trailing spaces and newlines
        if not line or line.startswith("#"):
            continue  # Ignore empty lines and comments

        values = line.split()
        if len(values) == 1:
            num_points = int(values[0])  # Read the number of points
        elif len(values) == 2:
            x, y = map(int, values)
            points.append((x, y))  # Store points as tuples
        else:
            print(f"Warning: Skipping invalid line '{line}'", file=sys.stderr)

    return points


def euclidean_distance(p1, p2):
    """
    Calculates the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor(points):
    """
    Implements the Nearest-Neighbor Heuristic to compute an approximate TSP solution.
    Returns the ordered list of points in the computed tour.
    """
    if not points:
        return []

    # Start from the first point in the input list (ensures deterministic behavior)
    start_point = points[0]
    tour = [start_point]
    remaining_points = set(points[1:])  # Exclude the start point

    current_point = start_point
    while remaining_points:
        # Select the nearest unvisited point
        next_point = min(remaining_points, key=lambda p: euclidean_distance(current_point, p))
        tour.append(next_point)
        remaining_points.remove(next_point)
        current_point = next_point

    # Return to the starting point to close the cycle
    tour.append(start_point)

    return tour

def print_tour(tour):
    """
    Prints the computed tour in the required format:
    - First line: number of points (excluding the duplicated start/end point).
    - Each subsequent line contains the (x, y) coordinates of a point.
    """
    print(len(tour) - 1)  # Number of points in the tour
    for x, y in tour[:-1]:  # Exclude the last repeated point
        print(x, y)

#===================== Main function ===================================================================#
def main():
    
    points = read_tsp_stdin()  # Read points from standard input.

    if not points:
        print("Error: No points were read from input.")
        return

    # Compute the Nearest-Neighbor tour
    tour = nearest_neighbor(points)

    print_tour(tour)

if __name__ == "__main__":
    main()

