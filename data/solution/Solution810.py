import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # Calculate the initial XOR of all elements
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # If the initial XOR is 0, Alice wins immediately
        if total_xor == 0:
            return True
        
        # If the number of elements is even, Alice wins
        # because she can always force Bob into a losing position
        return len(nums) % 2 == 0

def xorGame(nums: List[int]) -> bool:
    return Solution().xorGame(nums)