import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # Sort the beans array
        beans.sort()
        n = len(beans)
        total_beans = sum(beans)
        min_removal = float('inf')
        
        # Calculate the minimum removal for each possible number of beans in the remaining bags
        for i, x in enumerate(beans):
            # Beans to keep if all remaining bags have x beans
            beans_to_keep = x * (n - i)
            # Beans to remove
            beans_to_remove = total_beans - beans_to_keep
            # Update the minimum removal
            min_removal = min(min_removal, beans_to_remove)
        
        return min_removal

def minimumRemoval(beans: List[int]) -> int:
    return Solution().minimumRemoval(beans)