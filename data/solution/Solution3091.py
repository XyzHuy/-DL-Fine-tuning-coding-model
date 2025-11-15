import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0
        
        min_operations = float('inf')
        
        # We iterate over possible values of x
        for x in range(1, k + 1):
            # Calculate the minimum number of duplications needed
            n = (k + x - 1) // x  # Equivalent to math.ceil(k / x)
            # Calculate the total operations
            operations = (x - 1) + (n - 1)
            # Update the minimum operations found
            if operations < min_operations:
                min_operations = operations
        
        return min_operations

def minOperations(k: int) -> int:
    return Solution().minOperations(k)