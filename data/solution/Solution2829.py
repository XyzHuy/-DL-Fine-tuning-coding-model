import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # Initialize an empty set to store the elements of the k-avoiding array
        k_avoiding_set = set()
        # Start with the smallest positive integer
        current_number = 1
        
        # Continue until we have found n elements
        while len(k_avoiding_set) < n:
            # Check if adding the current number would violate the k-avoiding condition
            if k - current_number not in k_avoiding_set:
                k_avoiding_set.add(current_number)
            # Move to the next positive integer
            current_number += 1
        
        # Return the sum of the elements in the k-avoiding array
        return sum(k_avoiding_set)

def minimumSum(n: int, k: int) -> int:
    return Solution().minimumSum(n, k)