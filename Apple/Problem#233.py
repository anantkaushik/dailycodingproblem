"""
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""
def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	a,b = 0,1
	for _ in range(3,n+1):
		a,b = b,a + b
	return b