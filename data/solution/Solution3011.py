import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_set_bits(n: int) -> int:
            return bin(n).count('1')
        
        # Create a list of tuples (num, set_bits_count)
        nums_with_bits = [(num, count_set_bits(num)) for num in nums]
        
        # Try to sort the array using adjacent swaps with the same set bit count
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    # Check if they have the same number of set bits
                    if nums_with_bits[j][1] == nums_with_bits[j + 1][1]:
                        # Swap
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                        nums_with_bits[j], nums_with_bits[j + 1] = nums_with_bits[j + 1], nums_with_bits[j]
        
        # Check if the array is sorted
        return nums == sorted(nums)

def canSortArray(nums: List[int]) -> bool:
    return Solution().canSortArray(nums)