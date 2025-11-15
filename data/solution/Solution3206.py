import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        
        # Check for alternating groups in the circle
        for i in range(n):
            if colors[i] != colors[(i + 1) % n] and colors[(i + 1) % n] != colors[(i + 2) % n]:
                count += 1
        
        return count

def numberOfAlternatingGroups(colors: List[int]) -> int:
    return Solution().numberOfAlternatingGroups(colors)