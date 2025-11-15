import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index = 0
        odd_index = 1
        n = len(nums)
        
        while even_index < n and odd_index < n:
            if nums[even_index] % 2 == 0:
                even_index += 2
            elif nums[odd_index] % 2 == 1:
                odd_index += 2
            else:
                # Swap elements at even_index and odd_index
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
                even_index += 2
                odd_index += 2
        
        return nums

def sortArrayByParityII(nums: List[int]) -> List[int]:
    return Solution().sortArrayByParityII(nums)