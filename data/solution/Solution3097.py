import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Function to update the bit count when adding a number
        def add_number(bit_count, num):
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] += 1

        # Function to update the bit count when removing a number
        def remove_number(bit_count, num):
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] -= 1

        # Function to calculate the current OR value from bit count
        def current_or(bit_count):
            current_or_value = 0
            for i in range(32):
                if bit_count[i] > 0:
                    current_or_value |= (1 << i)
            return current_or_value

        n = len(nums)
        bit_count = [0] * 32  # To keep track of the count of each bit position
        left = 0
        min_length = float('inf')
        current_or_value = 0

        for right in range(n):
            add_number(bit_count, nums[right])
            current_or_value |= nums[right]

            # Shrink the window from the left as long as the current OR value is at least k
            while left <= right and current_or_value >= k:
                min_length = min(min_length, right - left + 1)
                remove_number(bit_count, nums[left])
                current_or_value = current_or(bit_count)
                left += 1

        return min_length if min_length != float('inf') else -1

def minimumSubarrayLength(nums: List[int], k: int) -> int:
    return Solution().minimumSubarrayLength(nums, k)