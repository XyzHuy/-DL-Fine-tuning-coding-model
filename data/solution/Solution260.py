import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all the numbers to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a set bit in the xor_all (rightmost set bit in this case)
        diff_bit = xor_all & -xor_all
        
        # Step 3: Divide numbers into two groups based on the set bit and XOR each group
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]

def singleNumber(nums: List[int]) -> List[int]:
    return Solution().singleNumber(nums)