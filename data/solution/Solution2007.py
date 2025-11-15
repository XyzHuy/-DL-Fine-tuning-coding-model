import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        # Count the frequency of each number in the changed array
        count = Counter(changed)
        original = []
        
        # Sort the changed array to handle the smallest elements first
        for x in sorted(changed):
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return []
            
            # Add the current element to the original array
            original.append(x)
            # Decrease the count of the current element and its double
            count[x] -= 1
            count[2 * x] -= 1
        
        return original

def findOriginalArray(changed: List[int]) -> List[int]:
    return Solution().findOriginalArray(changed)