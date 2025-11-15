import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        
        # If there is already at least one '1' in the array, we can make all elements 1
        if total_ones > 0:
            return n - total_ones
        
        # Try to find the smallest subarray whose gcd is 1
        min_length = float('inf')
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_length = min(min_length, j - i + 1)
                    break
        
        # If no such subarray is found, return -1
        if min_length == float('inf'):
            return -1
        
        # To make all elements 1, we need to make one element 1 first (min_length - 1 operations)
        # Then we can make the rest of the elements 1 (n - 1 operations)
        return min_length - 1 + n - 1

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)