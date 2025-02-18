import factorial

# manual_test_factorial.py

from factorial import calculate_factorial

def manual_test_factorial():
    # Test Case 1
    result = calculate_factorial(0)
    expected = 1
    print(f"Test Case 1: Result={result}, Expected={expected}")
    try:
        assert result == expected, "Test Case 1 failed!"
    except AssertionError as e:
        print(f"AssertionError: {e}")

    # Test Case 2
    result = calculate_factorial(5)
    expected = 120
    print(f"Test Case 2: Result={result}, Expected={expected}")
    try:
        assert result == expected, "Test Case 2 failed!"
    except AssertionError as e:
        print(f"AssertionError: {e}")

    # Test Case 3
    result = calculate_factorial(6)
    expected = 24  # Incorrect expectation
    print(f"Test Case 3: Result={result}, Expected={expected}")
    try:
        assert result == expected, "Test Case 3 failed!"
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    manual_test_factorial()