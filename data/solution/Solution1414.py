import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Generate all Fibonacci numbers less than or equal to k
        fibs = [1, 1]
        while True:
            next_fib = fibs[-1] + fibs[-2]
            if next_fib > k:
                break
            fibs.append(next_fib)
        
        # Use a greedy approach to find the minimum number of Fibonacci numbers that sum up to k
        count = 0
        while k > 0:
            # Find the largest Fibonacci number less than or equal to k
            while fibs and fibs[-1] > k:
                fibs.pop()
            k -= fibs.pop()
            count += 1
        
        return count

def findMinFibonacciNumbers(k: int) -> int:
    return Solution().findMinFibonacciNumbers(k)