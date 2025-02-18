"""
Illuminati Spotti - Counting Triangles in an Undirected Graph

### How the program solves the problem:
1. Read the adjacency matrix representing the graph.
2. Iterate through all possible triplets (i, j, k) where i < j < k.
3. Check if all three cities are directly connected to form a triangle.
4. Count and output the total number of triangles found.

### Time Complexity:
- The algorithm iterates through all unique triplets (i, j, k), which results in O(n³) complexity.

"""

def count_triangles(n, adj_matrix):
    triangle_count = 0
    
    # Iterate through all unique triplets of cities (i, j, k) where i < j < k
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if all three nodes are connected to form a triangle
                if adj_matrix[i][j] == 1 and adj_matrix[j][k] == 1 and adj_matrix[k][i] == 1:
                    triangle_count += 1
    
    return triangle_count

def main():
    # Read the number of cities (nodes)
    nodes = int(input())
    adj_matrix = []

    # Read the adjacency matrix
    for _ in range(nodes):
        row = list(map(int, input().split()))
        adj_matrix.append(row)

    # Calculate the number of triangles
    num_triangles = count_triangles(nodes, adj_matrix)

    # Print the result
    print(num_triangles)


if __name__ == "__main__":
    main()
