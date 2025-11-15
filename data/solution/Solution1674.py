import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (2 * limit + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            small, large = min(a, b), max(a, b)
            
            # Increment the range where one move is needed
            prefix_sum[1] += 2
            prefix_sum[small + 1] -= 1
            prefix_sum[large + limit + 1] += 1
            
            # No moves needed for the current sum
            prefix_sum[a + b] -= 1
            prefix_sum[a + b + 1] += 1
        
        # Calculate the minimum number of moves
        min_moves = float('inf')
        current_moves = 0
        
        for total in range(1, 2 * limit + 1):
            current_moves += prefix_sum[total]
            min_moves = min(min_moves, current_moves)
        
        return min_moves

def minMoves(nums: List[int], limit: int) -> int:
    return Solution().minMoves(nums, limit)