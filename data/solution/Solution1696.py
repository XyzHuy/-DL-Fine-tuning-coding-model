import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        heap = [(-nums[0], 0)]  # max-heap (using negative values)
        
        for i in range(1, n):
            # Remove elements from the heap that are out of the k range
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            
            # The root of the heap is the max score within the last k steps
            dp[i] = nums[i] - heap[0][0]
            
            # Push the current score and index onto the heap
            heapq.heappush(heap, (-dp[i], i))
        
        return dp[-1]

def maxResult(nums: List[int], k: int) -> int:
    return Solution().maxResult(nums, k)