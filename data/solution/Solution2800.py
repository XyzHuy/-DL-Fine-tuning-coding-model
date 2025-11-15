import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(x: str, y: str) -> str:
            # Check if y is already a substring of x
            if y in x:
                return x
            # Find the maximum overlap between x and y
            for i in range(len(y), 0, -1):
                if x.endswith(y[:i]):
                    return x + y[i:]
            return x + y
        
        # Generate all permutations of [a, b, c]
        from itertools import permutations
        
        # List to store all possible merged strings
        candidates = []
        
        for p in permutations([a, b, c]):
            # Merge the strings in the order of the permutation
            merged = merge(merge(p[0], p[1]), p[2])
            candidates.append(merged)
        
        # Find the lexicographically smallest string among the candidates with minimum length
        result = min(candidates, key=lambda x: (len(x), x))
        
        return result

def minimumString(a: str, b: str, c: str) -> str:
    return Solution().minimumString(a, b, c)