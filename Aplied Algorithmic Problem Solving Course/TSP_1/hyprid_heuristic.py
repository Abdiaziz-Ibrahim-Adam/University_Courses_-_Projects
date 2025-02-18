import sys
import math

"""
Hybrid Heuristic for the Traveling Salesman Problem (TSP)
----------------------------------------------------------
This program implements a hybrid heuristic.


### Solution Approach:
1. Read Input: Parse points from standard input, ignoring comments and empty lines.
2. Find Two Farthest Points: Selects the two points that are the farthest apart 
   to serve as initial starting points. This ensures a good spread for path-building.
3. Expand Both Ends Using Nearest Neighbor:
   - Greedily expands both tours by adding the closest unvisited point.
   - This step continues until all points are included in either of the two growing paths.
4. Merge the Two Paths:
   - The two paths are connected optimally by evaluating the best merging direction.
5. Close the Tour: Ensures the final tour forms a cycle by connecting the 
   last point back to the first.

"""

# ---------------- Step 1: Read Input ---------------- #

def read_tsp_stdin():
    """
    Reads input from standard input and returns a list of points (x, y).
    Ignores comment lines starting with '#' and skips empty lines.
    """
    points = []
    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # Ignore empty lines and comments
        values = line.split()
        if len(values) == 2:
            x, y = map(int, values)
            points.append((x, y))
        else:
            print(f"Warning: Skipping invalid line '{line}'", file=sys.stderr)
    return points

# ---------------- Step 2: Distance Calculation ---------------- #

def euclidean_distance(p1, p2):
    """
    Calculates the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# ---------------- Step 3: Hybrid Heuristic ---------------- #

def find_farthest_points(points):
    """
    Finds the two farthest points in the given list.
    """
    max_dist = -1
    farthest_pair = (points[0], points[1])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist > max_dist:
                max_dist = dist
                farthest_pair = (points[i], points[j])
    return farthest_pair

def hybrid_tsp(points):
    """
    Implements the hybrid heuristic starting from the two farthest points.
    """
    if len(points) < 2:
        return points
    
    start1, start2 = find_farthest_points(points)
    remaining = set(points)
    remaining.remove(start1)
    remaining.remove(start2)
    
    tour1 = [start1]
    tour2 = [start2]
    
    while remaining:
        if tour1 and remaining:
            next1 = min(remaining, key=lambda p: euclidean_distance(tour1[-1], p))
            tour1.append(next1)
            remaining.remove(next1)
        if tour2 and remaining:
            next2 = min(remaining, key=lambda p: euclidean_distance(tour2[-1], p))
            tour2.append(next2)
            remaining.remove(next2)
    
    # Merge the two paths optimally
    if euclidean_distance(tour1[-1], tour2[0]) < euclidean_distance(tour2[-1], tour1[0]):
        tour1.extend(tour2)
    else:
        tour1.extend(reversed(tour2))
    
    # Close the cycle
    tour1.append(tour1[0])
    return tour1

# ---------------- Step 4: Print the Final Tour ---------------- #

def print_tour(tour):
    """
    Prints the computed tour in the required format:
    - First line: number of points.
    - Each subsequent line contains the (x, y) coordinates of a point.
    """
    print(len(tour) - 1)  # Number of points in the tour
    for x, y in tour[:-1]:  # Exclude last repeated point
        print(x, y)

# ---------------- Main Execution ---------------- #

def main():
    points = read_tsp_stdin()  # Read input points
    if not points:
        print("Error: No points were read from input.")
        return
    
    tour = hybrid_tsp(points)  # Compute the hybrid heuristic TSP tour
    print_tour(tour)  # Output the final tour
    
if __name__ == "__main__":
    main()
