"""
* Hard TSP Instance Generator - Randomly Placed Points *

This program generates a "hard" Traveling Salesman Problem (TSP) instance by placing points at random distances 
from each other in a 2D plane. 

### Solution Approach:
1. Start at (0,0): The first point is placed at the origin.
2. Generate N-1 additional points:
   - Each point is placed at a random distance from the previous point.
   - A random direction (angle in radians) is chosen for each step.
   - The distance is randomly selected within a defined range (`min_dist` to `max_dist`).
3. Shuffle the points: This disrupts any inherent ordering, making the problem harder.
4. Output the points in TSP format: 
   - The first line contains the number of points.
   - The following lines contain the `(x, y)` coordinates of each point.

"""

import sys
import random
import math

def generate_random_tsp(n, min_dist=10, max_dist=100):
    """
    Generates `n` points where each point is placed at a random distance
    from the previous point.

    - `min_dist`: Minimum step distance between consecutive points.
    - `max_dist`: Maximum step distance between consecutive points.
    """
    print(f"# Hard TSP Instance with {n} randomly placed points")
    print(n)

    x, y = 0, 0  # Start at (0,0)
    points = [(x, y)]

    for _ in range(n - 1):
        angle = random.uniform(0, 2 * math.pi)  # Random direction
        distance = random.uniform(min_dist, max_dist)  # Random step distance
        x += round(distance * math.cos(angle))
        y += round(distance * math.sin(angle))
        points.append((x, y))

    # Randomize point order to make it even harder
    random.shuffle(points)

    for x, y in points:
        print(x, y)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_random_tsp.py <num_points>")
        sys.exit(1)

    n = int(sys.argv[1])
    generate_random_tsp(n)
