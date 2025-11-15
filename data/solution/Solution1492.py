import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        # Iterate only up to the square root of n to reduce complexity
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                # Check if i is not the square root of n to avoid duplication
                if i != n // i:
                    factors.append(n // i)
        
        # Sort the factors list
        factors.sort()
        
        # Return the k-th factor if it exists, otherwise return -1
        return factors[k - 1] if k <= len(factors) else -1

def kthFactor(n: int, k: int) -> int:
    return Solution().kthFactor(n, k)