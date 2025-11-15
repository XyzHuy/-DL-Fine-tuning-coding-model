import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        count = 0
        
        for roll in rolls:
            if roll not in seen:
                seen.add(roll)
                if len(seen) == k:
                    count += 1
                    seen.clear()
        
        return count + 1

def shortestSequence(rolls: List[int], k: int) -> int:
    return Solution().shortestSequence(rolls, k)