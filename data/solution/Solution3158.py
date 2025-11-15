import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        # Dictionary to count occurrences of each number
        count = {}
        # Result variable to store the XOR of duplicates
        result = 0
        
        # Count the occurrences of each number in the array
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # XOR all numbers that appear twice
        for num, cnt in count.items():
            if cnt == 2:
                result ^= num
        
        return result

def duplicateNumbersXOR(nums: List[int]) -> int:
    return Solution().duplicateNumbersXOR(nums)