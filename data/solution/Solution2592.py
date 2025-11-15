import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # Sort the nums array
        nums.sort()
        
        # Initialize the count of great elements
        greatness = 0
        # Initialize a pointer for the nums array
        j = 0
        
        # Iterate over a sorted copy of nums
        for num in sorted(nums):
            # Find the smallest element in the sorted nums that is greater than the current element
            if nums[j] < num:
                greatness += 1
                j += 1
        
        return greatness

# Example usage:
# sol = Solution()
# print(sol.maximizeGreatness([1,3,5,2,1,3,1]))  # Output: 4
# print(sol.maximizeGreatness([1,2,3,4]))        # Output: 3

def maximizeGreatness(nums: List[int]) -> int:
    return Solution().maximizeGreatness(nums)