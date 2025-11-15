import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize prefix sum array
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        # Deque to store indices of the prefix sums
        dq = deque()
        min_length = float('inf')
        
        for i in range(len(prefix_sum)):
            # Check if the current prefix sum minus the prefix sum at the front of the deque is at least k
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            # Maintain the increasing order of prefix sums in the deque
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            # Add the current index to the deque
            dq.append(i)
        
        # Return the result
        return min_length if min_length != float('inf') else -1

def shortestSubarray(nums: List[int], k: int) -> int:
    return Solution().shortestSubarray(nums, k)