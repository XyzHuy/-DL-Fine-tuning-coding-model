import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # Find all starting indices of substring 'a' in string 's'
        indices_a = [i for i in range(len(s) - len(a) + 1) if s[i:i + len(a)] == a]
        
        # Find all starting indices of substring 'b' in string 's'
        indices_b = [i for i in range(len(s) - len(b) + 1) if s[i:i + len(b)] == b]
        
        beautiful_indices = []
        
        # For each index in indices_a, check if there is a corresponding index in indices_b within the range k
        for i in indices_a:
            for j in indices_b:
                if abs(i - j) <= k:
                    beautiful_indices.append(i)
                    break  # No need to check further for this i, as we need only one corresponding j
        
        return beautiful_indices

def beautifulIndices(s: str, a: str, b: str, k: int) -> List[int]:
    return Solution().beautifulIndices(s, a, b, k)