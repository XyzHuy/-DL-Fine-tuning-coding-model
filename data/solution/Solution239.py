import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        # Deque to store indices of elements in the current window
        deq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove elements not within the sliding window
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove elements smaller than the current element from the deque
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # Add the current element's index to the deque
            deq.append(i)
            
            # The front of the deque is the largest element's index for the current window
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    return Solution().maxSlidingWindow(nums, k)