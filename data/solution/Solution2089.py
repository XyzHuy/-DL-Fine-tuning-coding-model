import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Sort the nums array in non-decreasing order
        nums.sort()
        
        # Find the indices where the sorted nums array equals the target
        target_indices = [i for i, num in enumerate(nums) if num == target]
        
        return target_indices

def targetIndices(nums: List[int], target: int) -> List[int]:
    return Solution().targetIndices(nums, target)