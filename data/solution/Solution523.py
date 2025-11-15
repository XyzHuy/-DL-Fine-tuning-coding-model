import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the modulus and its corresponding index
        modulus_index_map = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            if k != 0:
                current_sum %= k
            
            if current_sum in modulus_index_map:
                if i - modulus_index_map[current_sum] > 1:
                    return True
            else:
                modulus_index_map[current_sum] = i
        
        return False

def checkSubarraySum(nums: List[int], k: int) -> bool:
    return Solution().checkSubarraySum(nums, k)