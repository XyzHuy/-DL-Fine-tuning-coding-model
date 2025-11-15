import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array to use binary search
        potions.sort()
        m = len(potions)
        pairs = []
        
        for spell in spells:
            # Calculate the minimum potion strength required for a successful pair
            min_potion_strength = (success + spell - 1) // spell  # Equivalent to math.ceil(success / spell)
            # Use binary search to find the first potion that meets the strength requirement
            index = bisect_left(potions, min_potion_strength)
            # The number of successful pairs for this spell is the number of potions from index to the end
            pairs.append(m - index)
        
        return pairs

def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    return Solution().successfulPairs(spells, potions, success)