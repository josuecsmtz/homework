"""
Cover:
    Name: Josue de Jesus Castro Martinez
    ID: 2530263
    Group: IM 1-1
"""

"""
Executive Summary:
    The Fibonacci series is a sequence of numbers where each term is the sum
    of the two previous terms, starting with 0 and 1. Calculating the series
    up to n terms means printing the first n values of this sequence in order.
    This program reads an integer n from the user, validates that it is within
    an acceptable range and then uses a loop to generate and display the first
    n terms of the Fibonacci series on a single line.
"""

"""
Problem: Fibonacci series generator
Description:
    Program that reads an integer n and prints the first n terms of the
    Fibonacci series starting at 0 and 1.

Inputs:
    - n (int; number of terms to generate)

Outputs:
    - "Fibonacci series:" followed by the n terms separated by spaces

Validations:
    - n must be an integer
    - n must be >= 1
    - n must be <= 50 to avoid generating a very long series
    - If the validation fails, the program prints "Error: invalid input"
      and does not calculate the series.

Test cases:
    1) Normal:
        Input: n = 7
        Expected output:
            Fibonacci series: 0 1 1 2 3 5 8
    2) Border:
        Input: n = 1
        Expected output:
            Fibonacci series: 0
    3) Error:
        Input: n = 0
        Expected output:
            Error: invalid input
"""

# -----------------------------
# Fibonacci series main program
# -----------------------------

try:
    n = int(input("Enter n to calculate Fibonacci series: "))
except:
    print("Error: invalid input")
    exit()

# Validation: n must be between 1 and 50
if 1 <= n <= 50:
    print("Fibonacci series:", end=" ")

    # Initial values for Fibonacci
    a = 0
    b = 1
    result = 0

    # Same logic as original code: generate and print n terms
    for i in range(1, n + 1):
        print(f"{result}", end=" ")
        result = a + b
        b = a
        a = result

    print()  # final newline
else:
    print("Error: invalid input")
    exit()

"""
Conclusions:
    Using a loop makes it easy to generate the Fibonacci series term by term,
    only storing the last two values at each step. Handling special cases like
    small values of n (for example, n = 1) is important to keep the output
    consistent with the definition of the series. The same logic can be reused
    in other programs that need Fibonacci numbers, such as mathematical tools,
    recursive examples or performance tests for iterative algorithms.
"""

"""
References:
    1) Python documentation - for and while loops (docs.python.org)
    2) W3Schools - Python Loops and Examples of Fibonacci Series
    3) Class notes and course materials on Fibonacci sequence and loops in Python
"""