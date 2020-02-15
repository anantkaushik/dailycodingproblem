"""
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, 
using only O(1) space.
"""
# Time Complexity: O(n)
# Space Complexity: O(1)
def fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b