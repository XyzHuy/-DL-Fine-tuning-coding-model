import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # Calculate the net shift amount
        net_shift = 0
        for direction, amount in shift:
            if direction == 0:
                net_shift -= amount  # Left shift
            else:
                net_shift += amount  # Right shift
        
        # Normalize the net shift to be within the bounds of the string length
        n = len(s)
        net_shift = net_shift % n
        
        # Perform the shift
        if net_shift > 0:
            # Right shift
            return s[-net_shift:] + s[:-net_shift]
        else:
            # Left shift
            net_shift = -net_shift
            return s[net_shift:] + s[:net_shift]

def stringShift(s: str, shift: List[List[int]]) -> str:
    return Solution().stringShift(s, shift)