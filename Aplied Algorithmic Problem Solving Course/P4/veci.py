"""
* 4 Veci - Finding the Next Bigger Permutation
   This program takes an integer `X` and finds the smallest number greater than `X` that has the same digits.
   If no such number exists, it returns `0`.

* Solution Approach:
   1. Convert the number into a list of digits.
   2. Find the rightmost decreasing pair (`i` where `digits[i] < digits[i+1]`).
   3. Find the smallest digit on the right that is still greater than `digits[i]` and swap them.
   4. Reverse the order of the digits after index `i`.
   5. Convert back to an integer and return.

* Time Complexity:
   - Finding `i`: O(n)
   - Finding `j`: O(n)
   - Swapping: O(1)
   - Reversing: O(n)
   - Total Complexity: O(n)
"""

def next_bigger_permutation(digits):
    # Find the rightmost `i` where digits[i] < digits[i+1]
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # If no such index exists, return 0 (already largest number possible)
    if i == -1:
        return 0

    # Find the **smallest digit greater than `digits[i]`** in `digits[i+1:]`
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swap `digits[i]` and `digits[j]`
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse everything **after index `i`** (instead of sorting)
    digits[i + 1:] = reversed(digits[i + 1:])

    # Convert list back to integer
    return int("".join(map(str, digits)))

def main():
    # Read input 
    X = int(input().strip())  
    digits = list(map(int, str(X)))  # Convert number to list of digits

    # Compute the next bigger permutation
    print(next_bigger_permutation(digits))  

if __name__ == "__main__":
    main()
