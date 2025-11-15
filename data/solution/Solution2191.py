import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num: int) -> int:
            if num == 0:
                return mapping[0]
            mapped_num = 0
            power = 1
            while num > 0:
                digit = num % 10
                mapped_num += mapping[digit] * power
                num //= 10
                power *= 10
            return mapped_num

        # Create a list of tuples (mapped_value, original_index, original_number)
        mapped_nums = [(map_number(num), i, num) for i, num in enumerate(nums)]
        
        # Sort the list of tuples by mapped_value, then by original_index to maintain relative order
        mapped_nums.sort(key=lambda x: (x[0], x[1]))
        
        # Extract the original numbers in the new order
        sorted_nums = [num for _, _, num in mapped_nums]
        
        return sorted_nums

def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:
    return Solution().sortJumbled(mapping, nums)