import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # Calculate the maximum subsequence sum (sum of all positive numbers)
        max_sum = sum(max(num, 0) for num in nums)
        
        # Convert all numbers to their absolute values
        nums = [abs(num) for num in nums]
        
        # Sort the absolute values
        nums.sort()
        
        # Min-heap to keep track of the subsequence sums
        min_heap = [(0, 0)]  # (current sum, index of the next number to consider)
        
        # Iterate to find the k-th largest sum
        for _ in range(k - 1):
            current_sum, i = heapq.heappop(min_heap)
            
            if i < len(nums):
                # Push the sum including the next number
                heapq.heappush(min_heap, (current_sum + nums[i], i + 1))
                
                if i > 0:
                    # Push the sum including the next number but excluding the previous one
                    heapq.heappush(min_heap, (current_sum + nums[i] - nums[i - 1], i + 1))
        
        # The k-th largest sum is the negative of the smallest sum in the heap
        return max_sum - heapq.heappop(min_heap)[0]

def kSum(nums: List[int], k: int) -> int:
    return Solution().kSum(nums, k)