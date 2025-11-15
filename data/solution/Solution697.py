import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Dictionary to store the frequency, first occurrence, and last occurrence of each number
        num_info = {}
        
        for index, num in enumerate(nums):
            if num in num_info:
                num_info[num][0] += 1  # Increment frequency
                num_info[num][2] = index  # Update last occurrence
            else:
                num_info[num] = [1, index, index]  # Initialize frequency, first occurrence, and last occurrence
        
        # Find the degree of the array
        degree = max(info[0] for info in num_info.values())
        
        # Find the shortest subarray with the same degree
        min_length = float('inf')
        for info in num_info.values():
            if info[0] == degree:
                min_length = min(min_length, info[2] - info[1] + 1)
        
        return min_length

def findShortestSubArray(nums: List[int]) -> int:
    return Solution().findShortestSubArray(nums)