import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        perm = []
        
        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:  # char == 'D'
                perm.append(high)
                high -= 1
        
        # Append the last remaining number
        perm.append(low)  # or perm.append(high), since low == high at this point
        
        return perm

def diStringMatch(s: str) -> List[int]:
    return Solution().diStringMatch(s)