import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList(nums[:k])
        medians = []
        
        for i in range(k - 1, len(nums)):
            # Add the median of the current window to the result
            if k % 2 == 1:
                medians.append(window[k // 2])
            else:
                medians.append((window[k // 2] + window[k // 2 - 1]) / 2.0)
            
            # Slide the window: remove the element that is sliding out of the window
            if i + 1 < len(nums):
                window.remove(nums[i - k + 1])
                window.add(nums[i + 1])
        
        return medians

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    return Solution().medianSlidingWindow(nums, k)