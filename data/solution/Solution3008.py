import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # Find all starting indices of substring a in s
        indices_a = [i for i in range(len(s) - len(a) + 1) if s[i:i + len(a)] == a]
        # Find all starting indices of substring b in s
        indices_b = [i for i in range(len(s) - len(b) + 1) if s[i:i + len(b)] == b]
        
        beautiful_indices = []
        
        # Use two pointers to find beautiful indices
        i, j = 0, 0
        while i < len(indices_a) and j < len(indices_b):
            if abs(indices_a[i] - indices_b[j]) <= k:
                beautiful_indices.append(indices_a[i])
                i += 1
            elif indices_a[i] < indices_b[j]:
                i += 1
            else:
                j += 1
        
        return beautiful_indices

def beautifulIndices(s: str, a: str, b: str, k: int) -> List[int]:
    return Solution().beautifulIndices(s, a, b, k)