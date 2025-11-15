import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        
        for _ in range(volume):
            # Try to move left
            left = k
            while left > 0 and heights[left - 1] <= heights[left]:
                left -= 1
            while left < n - 1 and heights[left + 1] == heights[left]:
                left += 1
            
            if left < k:
                heights[left] += 1
                continue
            
            # Try to move right
            right = k
            while right < n - 1 and heights[right + 1] <= heights[right]:
                right += 1
            while right > 0 and heights[right - 1] == heights[right]:
                right -= 1
            
            if right > k:
                heights[right] += 1
                continue
            
            # Stay at the current position
            heights[k] += 1
        
        return heights

def pourWater(heights: List[int], volume: int, k: int) -> List[int]:
    return Solution().pourWater(heights, volume, k)