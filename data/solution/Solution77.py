import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            # If the current combination is of length k, add it to the result
            if len(path) == k:
                result.append(path[:])
                return
            # Iterate from the current start to n
            for i in range(start, n + 1):
                # Include i in the current combination
                path.append(i)
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack, remove i from the current combination
                path.pop()
        
        result = []
        backtrack(1, [])
        return result

def combine(n: int, k: int) -> List[List[int]]:
    return Solution().combine(n, k)