import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # Collect the indices of all 1's in the array
        indices = [i for i, num in enumerate(nums) if num == 1]
        
        # Initialize the result with a large number
        result = float('inf')
        
        # Use a sliding window approach to find the minimum moves
        for i in range(len(indices) - k + 1):
            # Calculate the median index of the current window
            median_index = indices[i + k // 2]
            
            # Calculate the total moves required to make all 1's in this window consecutive
            moves = 0
            for j in range(k):
                moves += abs(indices[i + j] - (median_index + j - k // 2))
            
            # Update the result with the minimum moves found
            result = min(result, moves)
        
        return result

def minMoves(nums: List[int], k: int) -> int:
    return Solution().minMoves(nums, k)