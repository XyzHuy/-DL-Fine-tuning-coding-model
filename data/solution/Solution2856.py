import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        # Count the frequency of each element
        freq = Counter(nums)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Calculate the minimum length after removals
        n = len(nums)
        if max_freq <= n // 2:
            # If the max frequency is less than or equal to half the length, we can remove all elements in pairs
            return n % 2
        else:
            # If the max frequency is more than half the length, the minimum length is the difference
            return max_freq * 2 - n if max_freq * 2 > n else n - max_freq * 2 + 1
        
# Example usage:
# sol = Solution()
# print(sol.minLengthAfterRemovals([1, 2, 3, 4]))  # Output: 0
# print(sol.minLengthAfterRemovals([1, 1, 2, 2, 3, 3]))  # Output: 0
# print(sol.minLengthAfterRemovals([1000000000, 1000000000]))  # Output: 2
# print(sol.minLengthAfterRemovals([2, 3, 4, 4, 4]))  # Output: 1

def minLengthAfterRemovals(nums: List[int]) -> int:
    return Solution().minLengthAfterRemovals(nums)