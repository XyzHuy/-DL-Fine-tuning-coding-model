import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        def can_equalize(target):
            total_loss = 0
            total_gain = 0
            
            for water in buckets:
                if water > target:
                    total_loss += (water - target) * (100 - loss) / 100
                else:
                    total_gain += target - water
            
            return total_loss >= total_gain
        
        low, high = 0, max(buckets)
        while high - low > 1e-5:
            mid = (low + high) / 2
            if can_equalize(mid):
                low = mid
            else:
                high = mid
        
        return low

def equalizeWater(buckets: List[int], loss: int) -> float:
    return Solution().equalizeWater(buckets, loss)