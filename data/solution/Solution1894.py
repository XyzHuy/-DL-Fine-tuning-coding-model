import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Calculate the total chalk used in one complete cycle
        total_chalk = sum(chalk)
        
        # Reduce k to the effective number of chalk pieces needed after complete cycles
        k = k % total_chalk
        
        # Iterate through the chalk array to find the student who will need to replace the chalk
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c

def chalkReplacer(chalk: List[int], k: int) -> int:
    return Solution().chalkReplacer(chalk, k)