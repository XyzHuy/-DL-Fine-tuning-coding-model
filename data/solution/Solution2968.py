import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        max_score = 0
        left = 0
        
        for right in range(n):
            mid = (left + right) // 2
            target = nums[mid]
            
            # Cost to make all elements from left to mid equal to target
            cost_left = target * (mid - left + 1) - (prefix_sum[mid + 1] - prefix_sum[left])
            
            # Cost to make all elements from mid+1 to right equal to target
            cost_right = (prefix_sum[right + 1] - prefix_sum[mid + 1]) - target * (right - mid)
            
            total_cost = cost_left + cost_right
            
            if total_cost <= k:
                max_score = max(max_score, right - left + 1)
            else:
                left += 1
        
        return max_score

def maxFrequencyScore(nums: List[int], k: int) -> int:
    return Solution().maxFrequencyScore(nums, k)