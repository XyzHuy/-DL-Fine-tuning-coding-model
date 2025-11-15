import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import combinations

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        target = total_sum / 2
        min_diff = float('inf')
        
        # Split the array into two halves
        left_half = nums[:n]
        right_half = nums[n:]
        
        # Generate all possible sums of subsets for both halves
        left_sums = [set() for _ in range(n + 1)]
        right_sums = [set() for _ in range(n + 1)]
        
        for i in range(n + 1):
            for comb in combinations(left_half, i):
                left_sums[i].add(sum(comb))
            for comb in combinations(right_half, i):
                right_sums[i].add(sum(comb))
        
        # Try to find the best combination
        for i in range(n + 1):
            left_sums[i] = sorted(left_sums[i])
            right_sums[n - i] = sorted(right_sums[n - i])
            
            j, k = 0, len(right_sums[n - i]) - 1
            while j < len(left_sums[i]) and k >= 0:
                current_sum = left_sums[i][j] + right_sums[n - i][k]
                min_diff = min(min_diff, abs(total_sum - 2 * current_sum))
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return min_diff

def minimumDifference(nums: List[int]) -> int:
    return Solution().minimumDifference(nums)