import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # Ensure x is less than or equal to y for easier calculations
        if x > y:
            x, y = y, x
        
        # Initialize the result array with zeros
        result = [0] * n
        
        # Function to calculate the distance between two houses considering the additional street
        def distance(i, j):
            return min(abs(i - j), abs(i - x) + 1 + abs(y - j), abs(i - y) + 1 + abs(x - j))
        
        # Iterate over all pairs of houses
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                d = distance(i, j)
                result[d - 1] += 2  # Count both (i, j) and (j, i)
        
        return result

def countOfPairs(n: int, x: int, y: int) -> List[int]:
    return Solution().countOfPairs(n, x, y)