import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        alternate = 0  # This will help in alternating between 0 and 1
        depth = 0
        
        for char in seq:
            if char == '(':
                depth += 1
                result.append(alternate)
                alternate = 1 - alternate  # Toggle between 0 and 1
            else:  # char == ')'
                alternate = 1 - alternate  # Toggle between 0 and 1
                result.append(alternate)
                depth -= 1
        
        return result

def maxDepthAfterSplit(seq: str) -> List[int]:
    return Solution().maxDepthAfterSplit(seq)