import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child_i = cookie_j = 0
        
        # Try to satisfy each child with the smallest available cookie
        while child_i < len(g) and cookie_j < len(s):
            if g[child_i] <= s[cookie_j]:
                # If the cookie can satisfy the child, move to the next child
                child_i += 1
            # Move to the next cookie in any case
            cookie_j += 1
        
        # The number of content children is equal to the number of greed factors we've satisfied
        return child_i

def findContentChildren(g: List[int], s: List[int]) -> int:
    return Solution().findContentChildren(g, s)