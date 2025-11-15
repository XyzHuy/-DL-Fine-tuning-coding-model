import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # To store indices of maximum elements
        min_deque = deque()  # To store indices of minimum elements
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Remove elements from max_deque that are smaller than nums[right]
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            # Remove elements from min_deque that are larger than nums[right]
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            
            # Add current element index to both deques
            max_deque.append(right)
            min_deque.append(right)
            
            # Check if the current window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                # Increment left pointer to make the window valid
                left += 1
                # Remove elements from deques that are out of the current window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length

def longestSubarray(nums: List[int], limit: int) -> int:
    return Solution().longestSubarray(nums, limit)