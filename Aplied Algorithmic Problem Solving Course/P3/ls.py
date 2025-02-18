"""
* ls - File Lister

    This program filters a list of filenames based on a given pattern that 
    includes wildcard characters ('*'). The wildcard '*' matches 
    zero or more characters of any kind.

* Solution Approach:
    1. Read the pattern `P` and the list of filenames.
    2. Split the pattern using `*`  to separate parts of a string so that we can get substrings .
    3. Then I ensure that the filename contains these substrings in the correct order:
       - If the pattern does not start with `*`, the filename must start with the first substring.
       - If the pattern does not end with `*`, the filename must end with the last substring.
       - All other substrings must appear in order, even if separated by other characters.
    4. Using `.find()` to check if each substring appears in sequence within the filename.

* Time Complexity:
    - Splitting the pattern into substrings: O(m) , with `m` being the length of the pattern.
    - Searching for each substring in a filename: O(n)
    - Checking all `N` filenames results in O(N * n) complexity. N represents the number of filenames in the input.
    n represents the length of the longest filename
    - Total Complexity: O(N * n)

"""


def matches_pattern(pattern, filename):
    """
    Matches a filename against a pattern with '*' wildcards.
    - '*' matches any sequence of characters (including empty).
    - The filename must contain the substrings in the correct order.
    - Ensures the first and last character constraints when '*' is not at the edges.
    """
    substring = pattern.split('*')  # Split pattern into substrings between '*'
    
    # If pattern starts with a normal character, filename must start with it
    if not pattern.startswith('*') and not filename.startswith(substring[0]):
        return False

    # If pattern ends with a normal character, filename must end with it
    if not pattern.endswith('*') and not filename.endswith(substring[-1]):
        return False

    # Try to find each substring in filename, ensuring correct order
    start_idx = 0  # Pointer to track position in filename
    for substr in substring:
        if substr:  # Ignore empty substrings caused by multiple '*'
            idx = filename.find(substr, start_idx)  # Find substr in filename
            if idx == -1:  # Not found → mismatch
                return False
            start_idx = idx + len(substr)  # Move start index after this match

    return True  # All substrs found in correct order

def ls(P, filenames):
    """Filters filenames that match the given pattern."""
    matched_files = [file for file in filenames if matches_pattern(P, file)]
    for file in matched_files:
        print(file)

def main():
    P = input().strip()  # Read pattern
    N = int(input().strip())  # Read number of filenames
    filenames = [input().strip() for _ in range(N)]  # Store filenames

    ls(P, filenames)

if __name__ == "__main__":
    main()
