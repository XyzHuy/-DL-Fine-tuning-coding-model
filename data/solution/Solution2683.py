import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        # Start with original[0] = 0
        original = [0] * n
        
        # Compute the rest of the original array
        for i in range(1, n):
            original[i] = original[i - 1] ^ derived[i - 1]
        
        # Check if the last element XORed with the first element matches derived[n-1]
        return original[n - 1] ^ original[0] == derived[n - 1]

def doesValidArrayExist(derived: List[int]) -> bool:
    return Solution().doesValidArrayExist(derived)