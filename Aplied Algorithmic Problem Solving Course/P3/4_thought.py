"""
* 4 Thought - Mathematical Expression Solver  
    This program, given an input `n`, will produce a mathematical expression using exactly four 4's 
    and exactly three operations from this set: {* , + , - , /}, which evaluates to `n`.

* Solution Approach:
    1. precalculation all valid expressions: using four `4`s and different operator combinations.
    2. Storing results: in a dictionary (`expressions_dict`) for fast lookup.
    3. For each test case: check if `n` exists in the dictionary and return the corresponding equation.
    4. If no valid equation exists, return "no solution".

* Time Complexity:
    - Generating expressions: `O(4³) = O(64)` (constant time)
    - Checking for a number in a dictionary: `O(1)` (fast lookup)
    - Total Complexity: `O(1)` 
"""

def generate_solutions():
    """
    Generates all possible expressions using exactly four 4's and three operations.
    Stores them in a dictionary for quick lookup.
    """
    mathematical_operations = ['+', '-', '*', '/']
    expressions = {}

    # Nested loops to generate all possible operator combinations
    for op1 in mathematical_operations:
        for op2 in mathematical_operations:
            for op3 in mathematical_operations:
                # Build the expression string
                expr_str = f"4 {op1} 4 {op2} 4 {op3} 4"

                # Evaluate the expression safely using integer division (// instead of /)
                try:
                    result = eval(expr_str.replace("/", "//"))
                    if result not in expressions:  # Store only the first valid equation
                        expressions[result] = expr_str
                except ZeroDivisionError:
                    continue  # Skip invalid expressions with division by zero

    return expressions

def main():
    # Read and validate the number of test cases
    while True:
        try:
            case_nums = int(input().strip())
            if 1 <= case_nums <= 1000:
                break
            else:
                print("Error: Number of test cases must be between 1 and 1000.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

    expressions_dict = generate_solutions()  # Precompute valid expressions

    for _ in range(case_nums):
        while True:
            try:
                n = int(input().strip())
                if -1_000_000 <= n <= 1_000_000:
                    break
                else:
                    print("Error: Number must be between -1,000,000 and 1,000,000.")
            except ValueError:
                print("Error: Invalid input. Please enter an integer.")

        if n in expressions_dict:
            print(f"{expressions_dict[n]} = {n}")  # Print valid equation
        else:
            print("no solution")  # If no valid equation exists

if __name__ == "__main__":
    main()
