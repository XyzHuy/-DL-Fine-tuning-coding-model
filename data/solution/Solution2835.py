import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        # Step 1: Check if the total sum of nums is less than target
        if sum(nums) < target:
            return -1
        
        # Step 2: Count the number of each power of 2 in nums
        power_count = Counter()
        for num in nums:
            power_count[num] += 1
        
        # Step 3: Initialize the number of operations
        operations = 0
        
        # Step 4: Iterate over the bits of the target
        current_sum = 0
        for i in range(32):  # Since target < 2^31, we only need to check up to 31 bits
            bit = (target >> i) & 1
            current_sum += (1 << i) * power_count[1 << i]
            
            if bit == 1:
                if current_sum < (1 << i):
                    # We need (1 << i) but we don't have it
                    # We need to split a higher power of 2
                    needed = (1 << i)
                    for j in range(i + 1, 32):
                        if power_count[1 << j] > 0:
                            power_count[1 << j] -= 1
                            operations += (j - i)
                            current_sum += (1 << i)
                            break
                        else:
                            current_sum += (1 << j)
                else:
                    # We already have (1 << i) covered
                    current_sum -= (1 << i)
        
        return operations

def minOperations(nums: List[int], target: int) -> int:
    return Solution().minOperations(nums, target)