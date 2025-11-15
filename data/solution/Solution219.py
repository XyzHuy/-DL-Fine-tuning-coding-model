import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each number
        last_seen = {}
        
        for i, num in enumerate(nums):
            if num in last_seen and abs(i - last_seen[num]) <= k:
                return True
            last_seen[num] = i
        
        return False

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    return Solution().containsNearbyDuplicate(nums, k)