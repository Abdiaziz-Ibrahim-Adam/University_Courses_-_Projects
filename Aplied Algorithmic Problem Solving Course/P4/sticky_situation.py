"""
* Sticky Situation - Checking if a valid triangle can be formed
   This program takes a list of stick lengths and determines if any three of them can form a triangle.

* Solution Approach:
   1. Read the stick lengths.
   2. Sort them in ascending order.
   3. Loop through consecutive triplets to check if they satisfy the triangle inequality.
   4. If a valid triangle is found, print `"possible"` and exit.
   5. Otherwise, print `"impossible"`.

* Time Complexity:
   - Sorting takes O(N log N)
   - Checking triplets takes O(N)
   - Total Complexity: O(N log N)
"""

def can_build_triangle(sticks):
    # Sorting the sticks in ascending order
    sticks.sort()
    
    # Loop through the sorted list, checking triplets
    for i in range(len(sticks) - 2):
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:  # Triangle Inequality
            print("possible")
            return  # Exiting early if we find a valid triangle
    
    # If no valid triangle found
    print("impossible")

def main():
    # Read input
    N = int(input().strip())  # Number of sticks
    sticks = list(map(int, input().split()))  # Reading all stick lengths as a list

    # Check if we can form a valid triangle
    can_build_triangle(sticks)

if __name__ == "__main__":
    main()
