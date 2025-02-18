"""
* The Plank
    This program determines the number of ways to construct a plank of length `n` 
    using wooden pieces of lengths 1, 2, and 3 meters. Each piece can be used any 
    number of times.

* Solution Approach:
    1. Using Dynamic Programming (DP) to avoid redundant calculations.
    2. Define `dp[i]` as the number of ways to build a plank of length `i`.
    3. Use the recurrence relation:
       - `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`
       - This considers that we can form `i` by adding `1m`, `2m`, or `3m` pieces 
         to previously solved subproblems.
    4. Compute values iteratively, storing results in an array to avoid recomputation.

* Base Cases:
    - `dp[0] = 1`  (One way to form length 0: do nothing)
    - `dp[1] = 1`  (Only one way: using a `1m` piece)
    - `dp[2] = 2`  (Two ways: `1+1` or `2`)

* Time Complexity:
    - O(n) → Since we compute `dp[i]` once for each `i` from `0` to `n`.
"""

def count_ways(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # One way to make length 0 (do nothing)
    dp[1] = 1  # One way to make length 1 (just one piece of length 1)
    dp[2] = 2  # Two ways: (1+1) or (2)

    # Fill DP table using the recurrence relation
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

def main():

    # --- Read Input --- #
    n = int(input().strip())

    print(count_ways(n))

if __name__ == "__main__" :
    main()
