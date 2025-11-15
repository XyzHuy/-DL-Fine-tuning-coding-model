import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)
        
        # Iterate over each bit position (0 to 30, since 2^30 > 10^9)
        for i in range(32):
            count_ones = 0
            # Count the number of 1s at the ith bit position
            for num in nums:
                count_ones += (num >> i) & 1
            # The number of 0s at the ith bit position
            count_zeros = n - count_ones
            # The total Hamming distance for the ith bit position
            total_distance += count_ones * count_zeros
        
        return total_distance

def totalHammingDistance(nums: List[int]) -> int:
    return Solution().totalHammingDistance(nums)