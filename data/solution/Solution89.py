import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        # Start with the base case for n = 1
        gray = [0, 1]
        
        # Generate the sequence iteratively for n > 1
        for i in range(1, n):
            # Reflect the current sequence and prefix with 1 (i.e., add 2^i)
            gray += [x + (1 << i) for x in reversed(gray)]
        
        return gray

def grayCode(n: int) -> List[int]:
    return Solution().grayCode(n)