import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # Identify numbers that appear on both the front and back of the same card
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        
        # Collect all possible numbers from fronts and backs, excluding those in 'same'
        possible_numbers = {x for x in fronts + backs if x not in same}
        
        # Return the minimum possible good integer, or 0 if there are none
        return min(possible_numbers) if possible_numbers else 0

def flipgame(fronts: List[int], backs: List[int]) -> int:
    return Solution().flipgame(fronts, backs)