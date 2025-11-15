import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Find the index of k
        idx_k = nums.index(k)
        n = len(nums)
        
        # Dictionary to store the count of imbalance values
        imbalance_count = defaultdict(int)
        imbalance_count[0] = 1  # Starting point
        
        # Traverse to the right of k
        imbalance = 0
        for i in range(idx_k + 1, n):
            imbalance += 1 if nums[i] > k else -1
            imbalance_count[imbalance] += 1
        
        # Traverse to the left of k (including k)
        result = 0
        imbalance = 0
        for i in range(idx_k, -1, -1):
            imbalance += 1 if nums[i] > k else -1 if nums[i] < k else 0
            # We need imbalance of 0 or 1 to have k as the median
            result += imbalance_count[-imbalance] + imbalance_count[1 - imbalance]
        
        return result

# Example usage:
# sol = Solution()
# print(sol.countSubarrays([3, 2, 1, 4, 5], 4))  # Output: 3
# print(sol.countSubarrays([2, 3, 1], 3))        # Output: 1

def countSubarrays(nums: List[int], k: int) -> int:
    return Solution().countSubarrays(nums, k)