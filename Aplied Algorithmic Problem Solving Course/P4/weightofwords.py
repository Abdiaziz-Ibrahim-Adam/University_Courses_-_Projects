"""
* weightofwords - Generate a word with given length and weight

* Solution Approach:
   1. Checking if forming such a word is possible:
      - The minimum possible weight is `L` (all 'a'), and the maximum possible weight is `L * 26` (all 'z').
      - If `W` is outside this range, returning `"impossible"`.
   2. Construct the word greedily:
      - Starting with an empty list `word = []`.
      - For each position in the word:
         - Find the largest possible letter (starting from 'z') that doesn't exceed `remaining_weight`.
         - Then add the letter to the `word` list and subtract its weight from `remaining_weight`.
   3. Convert the `word` list to a string and return the result.

* Time Complexity:
   - O(L x 26) ≈ O(L) (inner loop runs at most 26 times)
"""

def get_weighted_word(L, W):
    letters = "abcdefghijklmnopqrstuvwxyz"  # List of letters
    
    # Controlling if its even possible to form a string
    if W < L or W > L * 26:
        return "impossible"

    word = []
    remaining_weight = W

    for i in range(L):
        # Determining the highest possible letter without exceeding `remaining_weight`
        for j in range(25, -1, -1):  # Starting from 'z' (index 25) down to 'a' (index 0)
            if remaining_weight - (j + 1) >= (L - len(word) - 1):
                word.append(letters[j])  # Add the letter to the word
                remaining_weight -= (j + 1)
                break

    return "".join(word)  # Convert list to string


def main():
    L, W = map(int, input().split())  # Read input values
    print(get_weighted_word(L, W))   


if __name__ == "__main__":
    main()
