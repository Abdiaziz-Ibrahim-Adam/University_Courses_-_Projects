"""
* Radio Commercials

    This program finds the maximum possible profit that Onid Pizza can obtain 
    by selecting a continuous sequence of commercial breaks.

* Solution Approach:
    1. Convert the listener count for each commercial break into profit values:
       - Profit for each break is calculated as `profit[i] = listeners[i] - p`
       - This means that a commercial break is only profitable if `listeners[i] > p`
    2. Using a Divide & Conquer (Maximum Subarray Sum Algorithm) to find the 
       best possible continuous sequence of commercial breaks that maximizes profit.
    3. Then divide the array into left and right halves recursively, then find:
       - The max sum in the left half.
       - The max sum in the right half.
       - The max sum that spans across the middle.
    4. The answer is the maximum of these three values.

* Time Complexity:
    - Sorting and splitting: O(log n)
    - Finding max subarray sum in each half: O(n)
    - Combining results: O(n)
    - Total Complexity: O(n log n).

"""

def max_crossing_sum(arr, left, mid, right):
    """Find the maximum sum of a subarray that crosses the middle index."""
    # Compute max sum for the left half (from mid to left)
    left_sum = float('-inf')
    temp_sum = 0
    for i in range(mid, left - 1, -1):
        temp_sum += arr[i]
        left_sum = max(left_sum, temp_sum)

    # Compute max sum for the right half (from mid+1 to right)
    right_sum = float('-inf')
    temp_sum = 0
    for i in range(mid + 1, right + 1):
        temp_sum += arr[i]
        right_sum = max(right_sum, temp_sum)

    return left_sum + right_sum  # Return the best crossing sum

def max_subarray_sum(arr, left, right):
    """Recursively find the max subarray sum using divide & conquer."""
    if left == right:  # Base case: Only one element
        return arr[left]

    mid = (left + right) // 2  # Find middle index

    # Find max sum in left half, right half, and crossing the middle
    left_max = max_subarray_sum(arr, left, mid)
    right_max = max_subarray_sum(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)

def max_expected_profit(n, p, listeners):
    """Convert listeners to profit values and find max subarray sum."""
    profit_array = [students - p for students in listeners]  # Convert to profits
    return max_subarray_sum(profit_array, 0, n - 1)

# -------------------------- Main function -------------------------------------------#
def main():
    # --- Read Input ---
    n, p = map(int, input().split())  
    listeners = list(map(int, input().split()))  

    print(max_expected_profit(n, p, listeners))

if __name__ == "__main__" :
    main()