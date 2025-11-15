import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find the first non-negative number
        neg_count = bisect.bisect_left(nums, 0)
        
        # Find the first positive number
        pos_count = len(nums) - bisect.bisect_left(nums, 1)
        
        # Return the maximum of the two counts
        return max(neg_count, pos_count)

# Example usage:
# sol = Solution()
# print(sol.maximumCount([-2, -1, -1, 1, 2, 3]))  # Output: 3
# print(sol.maximumCount([-3, -2, -1, 0, 0, 1, 2]))  # Output: 3
# print(sol.maximumCount([5, 20, 66, 1314]))  # Output: 4

def maximumCount(nums: List[int]) -> int:
    return Solution().maximumCount(nums)