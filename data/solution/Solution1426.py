import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        # Create a set of the array elements for O(1) lookups
        elements_set = set(arr)
        count = 0
        
        # Iterate through each element in the array
        for x in arr:
            # Check if x + 1 is in the set
            if x + 1 in elements_set:
                count += 1
        
        return count

def countElements(arr: List[int]) -> int:
    return Solution().countElements(arr)