import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        # Iterate over each starting point of the subarray
        for i in range(n):
            current_gcd = nums[i]
            # Iterate over each ending point of the subarray starting from i
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                # If the GCD of the current subarray is k, increment the count
                if current_gcd == k:
                    count += 1
                # If the GCD becomes less than k, no need to check further
                elif current_gcd < k:
                    break
        
        return count

def subarrayGCD(nums: List[int], k: int) -> int:
    return Solution().subarrayGCD(nums, k)