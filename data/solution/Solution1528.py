import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create a list to hold the shuffled characters
        shuffled = [''] * len(s)
        
        # Place each character in its new position
        for char, index in zip(s, indices):
            shuffled[index] = char
        
        # Join the list into a string and return
        return ''.join(shuffled)

def restoreString(s: str, indices: List[int]) -> str:
    return Solution().restoreString(s, indices)