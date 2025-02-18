"""
* Robot Tour Optimization – Closest Pair Heuristic *

This program implements the Closest-Pair Heuristic for solving the Traveling Salesman Problem (TSP).
Instead of always choosing the nearest neighbor, it iteratively merges the closest available pairs
of points until a full cycle is formed.

* Solution Approach: *
1. Reading Input from Standard Input (sys.stdin)
   - The program expects a list of points (x, y) in the plane.
   - Lines starting with `#` are ignored as comments.
   - The first relevant line specifies the number of points.
   - The following lines contain `(x, y)` coordinates.

2. Initializing Chains
   - Each point starts as its own separate chain.
   - A priority queue (min-heap) is used to efficiently store and retrieve the closest pairs.

3. Merging Closest Pairs
   - The algorithm repeatedly finds the closest pair of endpoints.
   - It merges them into a single chain.
   - The process continues until only one cycle remains.

4. Finalizing the Tour
   - The last two endpoints are connected to form a cycle.
   - The result is printed in the required format.

"""

import sys
import math
import heapq

def read_tsp_stdin():
    points = []
    first_line_skipped = False

    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # Ignore empty lines and comments

        values = line.split()
        if len(values) == 1 and not first_line_skipped:
            first_line_skipped = True  # Skip first number line
            continue  

        if len(values) == 2:
            x, y = map(int, values)
            points.append((x, y))
        else:
            print(f"Warning: Skipping invalid line '{line}'", file=sys.stderr)

    return points



def euclidean_distance(p1, p2):
    """
    Calculates the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def initialize_closest_pairs(points):
    heap = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            heapq.heappush(heap, (distance, points[i], points[j]))

    return heap



def closest_pair(points):
    """
    Implements the Closest-Pair Heuristic for TSP.
    Builds a tour by merging the closest available pairs.
    """

    if not points:
        print("Error: No valid points were read from input.", file=sys.stderr)
        return []

    if len(points) == 1:
        return points  # If there's only one point, return it as the tour

    chains = {p: [p] for p in points}  # Initialize chains
    heap = initialize_closest_pairs(points)

    if not heap:  # If heap is empty, return an error message
        print("Error: No valid pairs found in the input.", file=sys.stderr)
        return []

    while len(chains) > 1:
        if not heap:
            return []
        
        distance, p1, p2 = heapq.heappop(heap)

        if p1 in chains and p2 in chains and chains[p1] != chains[p2]:

            # Ensure merging only unique elements
            new_chain = list(dict.fromkeys(chains[p1] + chains[p2]))  # Removes duplicates

            # Store old chains before deleting
            old_chain_p1 = chains[p1]
            old_chain_p2 = chains[p2]

            del chains[p1]
            del chains[p2]

            # Store the new chain under a single key
            merged_key = new_chain[0]  # Choose the first point as the key
            chains[merged_key] = new_chain

            # Add new distances between merged endpoints and remaining chains
            for p in points:
                if p not in new_chain and p in chains:
                    dist1 = euclidean_distance(new_chain[0], p)
                    dist2 = euclidean_distance(new_chain[-1], p)
                    heapq.heappush(heap, (dist1, new_chain[0], p))
                    heapq.heappush(heap, (dist2, new_chain[-1], p))

    # Ensuring only one chain remains
    remaining_keys = list(chains.keys())

    if len(remaining_keys) != 1:
        
        # Force merging the remaining chains
        final_chain = []
        for key in remaining_keys:
            final_chain.extend(chains[key])  # Merge all remaining chains

        # Remove duplicates and close the cycle
        final_chain = list(dict.fromkeys(final_chain))
        final_chain.append(final_chain[0])  # Close the loop

        return final_chain

    final_tour = chains[remaining_keys[0]]

    # Ensure it's a closed cycle
    if final_tour[0] != final_tour[-1]:
        final_tour.append(final_tour[0])

    return final_tour


def print_tour(tour):
    """
    Prints the computed tour in the required format:
    - First line: number of points (excluding the duplicated start/end point).
    - Each subsequent line contains the (x, y) coordinates of a point.
    """
    print(len(tour) - 1)  # Print total number of points in the tour
    for x, y in tour[:-1]:  # Exclude the last repeated point
        print(x, y)


#===================== Main function ===================================================================#
def main():
    """
    Main function to execute the Closest-Pair Heuristic for TSP.
    Reads input, computes the tour, and prints the result.
    """
    points = read_tsp_stdin()

    if not points:
        print("Error: No points were read from input.")
        return

    # Compute the Closest-Pair tour
    tour = closest_pair(points)

    print_tour(tour)


if __name__ == "__main__":
    main()
