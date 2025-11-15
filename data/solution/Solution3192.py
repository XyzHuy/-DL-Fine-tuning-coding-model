import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        flip_state = 0  # 0 means no flip, 1 means flip

        for num in nums:
            # If the current number is affected by a flip, it will be flipped
            effective_num = num ^ flip_state

            # If the effective number is 0, we need to flip from this point onwards
            if effective_num == 0:
                flip_state ^= 1  # Toggle the flip state
                operations += 1

        return operations

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)