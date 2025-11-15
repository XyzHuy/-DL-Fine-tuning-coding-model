import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperations(self, n: int) -> int:
        # The target value to which all elements should be equal is the median of the array.
        # For an array of length n, the median is the (n // 2)-th element in the sequence.
        # The sequence is [1, 3, 5, ..., (2*i) + 1, ..., (2*(n-1)) + 1]
        # The median is the (2 * (n // 2) + 1) for odd n, and the average of the two middle elements for even n.
        # However, due to symmetry, we can just consider the first half of the array.
        
        # Calculate the number of operations
        operations = 0
        for i in range(n // 2):
            operations += (n - 2 * i - 1)
        
        return operations

def minOperations(n: int) -> int:
    return Solution().minOperations(n)