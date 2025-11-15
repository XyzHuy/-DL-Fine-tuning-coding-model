import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # Transform the array to nums[i] - i
        transformed = [nums[i] - i for i in range(n)]
        
        # Coordinate compression
        sorted_transformed = sorted(set(transformed))
        rank = {val: idx for idx, val in enumerate(sorted_transformed)}
        
        # BIT (Fenwick Tree) to store the maximum sum of balanced subsequences
        bit = [0] * (len(sorted_transformed) + 1)
        
        def query(x: int) -> int:
            res = 0
            while x > 0:
                res = max(res, bit[x])
                x -= x & -x
            return res
        
        def update(x: int, val: int) -> None:
            while x < len(bit):
                bit[x] = max(bit[x], val)
                x += x & -x
        
        max_sum = float('-inf')
        
        for i in range(n):
            # Get the rank of the transformed value
            r = rank[transformed[i]]
            # Query the maximum sum of balanced subsequences ending before this value
            current_max = query(r + 1) + nums[i]
            # Update the BIT with the new maximum sum for this value
            update(r + 1, current_max)
            # Update the global maximum sum
            max_sum = max(max_sum, current_max)
        
        return max_sum if max_sum > 0 else max(nums)

def maxBalancedSubsequenceSum(nums: List[int]) -> int:
    return Solution().maxBalancedSubsequenceSum(nums)