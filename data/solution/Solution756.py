import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Create a mapping from pairs to possible tops
        rules = defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed:
            rules[a][b].append(c)
        
        # Use a stack to simulate the backtracking process
        stack = [(bottom, 0, [])]
        
        while stack:
            bottom, index, next_level = stack.pop()
            
            # If we have processed the entire level, move to the next level
            if index == len(bottom) - 1:
                if len(next_level) == 1:
                    return True
                bottom = next_level
                index = 0
                next_level = []
                stack.append((bottom, index, next_level))
                continue
            
            # Try all possible tops for the current pair
            for top in rules[bottom[index]][bottom[index + 1]]:
                stack.append((bottom, index + 1, next_level + [top]))
        
        return False

def pyramidTransition(bottom: str, allowed: List[str]) -> bool:
    return Solution().pyramidTransition(bottom, allowed)