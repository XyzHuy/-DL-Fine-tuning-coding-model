import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        # Iterate over all possible j and k pairs
        for j in range(1, n - 2):
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    # Count valid i's for the current j and k
                    i_count = sum(1 for i in range(j) if nums[i] < nums[k])
                    # Count valid l's for the current j and k
                    l_count = sum(1 for l in range(k + 1, n) if nums[l] > nums[j])
                    # Each combination of valid i and l forms a valid quadruplet
                    count += i_count * l_count
        
        return count

def countQuadruplets(nums: List[int]) -> int:
    return Solution().countQuadruplets(nums)