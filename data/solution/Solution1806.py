import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # Initial permutation
        perm = list(range(n))
        # Target permutation to reach back
        target = perm[:]
        # Variable to count the number of operations
        operations = 0
        
        while True:
            # Create a new array arr based on the given rules
            arr = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            # Increment the operation count
            operations += 1
            # Update perm to arr
            perm = arr
            # Check if perm is back to the initial permutation
            if perm == target:
                break
        
        return operations

def reinitializePermutation(n: int) -> int:
    return Solution().reinitializePermutation(n)