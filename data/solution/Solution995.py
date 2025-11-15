import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flip_status = [0] * (n + 1)  # To keep track of the flip operations
        flip_times = 0  # To keep track of the number of flips at the current position

        for i in range(n):
            # Update the flip_times based on the flip_status
            flip_times += flip_status[i]
            
            # If the current bit is 0 and flip_times is even, or if the current bit is 1 and flip_times is odd, we need to flip
            if (nums[i] == 0 and flip_times % 2 == 0) or (nums[i] == 1 and flip_times % 2 == 1):
                # If flipping is not possible (not enough elements left to form a subarray of length k)
                if i + k > n:
                    return -1
                # Mark the end of the flip operation
                flip_status[i + k] -= 1
                # Increment the flip_times
                flip_times += 1
                # Increment the flip_count
                flip_count += 1

        return flip_count

def minKBitFlips(nums: List[int], k: int) -> int:
    return Solution().minKBitFlips(nums, k)