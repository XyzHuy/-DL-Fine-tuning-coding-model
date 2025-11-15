import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        window_size = 2 * k + 1
        
        if window_size > n:
            return avgs
        
        window_sum = sum(nums[:window_size])
        avgs[k] = window_sum // window_size
        
        for i in range(k + 1, n - k):
            window_sum += nums[i + k] - nums[i - k - 1]
            avgs[i] = window_sum // window_size
        
        return avgs

def getAverages(nums: List[int], k: int) -> List[int]:
    return Solution().getAverages(nums, k)