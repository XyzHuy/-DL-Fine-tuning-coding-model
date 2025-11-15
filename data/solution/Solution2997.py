import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Calculate the XOR of all elements in nums
        current_xor = 0
        for num in nums:
            current_xor ^= num
        
        # Calculate the XOR difference between current_xor and k
        xor_difference = current_xor ^ k
        
        # The number of operations needed is the number of 1s in the binary representation of xor_difference
        return xor_difference.bit_count()

def minOperations(nums: List[int], k: int) -> int:
    return Solution().minOperations(nums, k)