import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for group in groups:
            # Try to find the current group in nums starting from index i
            while i < len(nums) - len(group) + 1:
                # Check if the subarray from i matches the current group
                if nums[i:i + len(group)] == group:
                    # Move i forward by the length of the current group to ensure disjointness
                    i += len(group)
                    break
                else:
                    # Move to the next index in nums
                    i += 1
            else:
                # If the group was not found in the remaining part of nums, return False
                return False
        # All groups were found in order and disjointly
        return True

def canChoose(groups: List[List[int]], nums: List[int]) -> bool:
    return Solution().canChoose(groups, nums)