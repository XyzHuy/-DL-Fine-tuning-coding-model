import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # Count the frequency of each number in the array
        count = Counter(arr)
        
        # Sort the array by absolute value to handle pairs correctly
        for x in sorted(arr, key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return False
            # Decrease the count of x and 2*x
            count[x] -= 1
            count[2 * x] -= 1
        
        return True

def canReorderDoubled(arr: List[int]) -> bool:
    return Solution().canReorderDoubled(arr)