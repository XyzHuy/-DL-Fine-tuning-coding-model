import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Sort the array to pair the smallest and largest elements
        nums.sort()
        # Initialize the maximum pair sum to a very small number
        max_pair_sum = 0
        # Pair the smallest element with the largest, second smallest with second largest, etc.
        for i in range(len(nums) // 2):
            pair_sum = nums[i] + nums[-(i + 1)]
            # Update the maximum pair sum if the current pair sum is larger
            max_pair_sum = max(max_pair_sum, pair_sum)
        return max_pair_sum

def minPairSum(nums: List[int]) -> int:
    return Solution().minPairSum(nums)