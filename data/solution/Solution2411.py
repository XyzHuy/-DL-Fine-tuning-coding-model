import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the result array with the maximum possible subarray length
        result = [1] * n
        
        # This will store the farthest index for each bit position (0-31) that contributes to the OR
        last = [0] * 32
        
        # Traverse the array from the end to the beginning
        for i in range(n - 1, -1, -1):
            # Update the last occurrence of each bit position
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            
            # Find the farthest index that contributes to the OR starting from index i
            farthest = max(last)
            # Calculate the length of the smallest subarray
            result[i] = max(1, farthest - i + 1)
        
        return result

def smallestSubarrays(nums: List[int]) -> List[int]:
    return Solution().smallestSubarrays(nums)