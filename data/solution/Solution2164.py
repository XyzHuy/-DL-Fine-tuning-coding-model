import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Extract elements at even and odd indices
        even_index_elements = [nums[i] for i in range(0, len(nums), 2)]
        odd_index_elements = [nums[i] for i in range(1, len(nums), 2)]
        
        # Sort even index elements in non-decreasing order
        even_index_elements.sort()
        
        # Sort odd index elements in non-increasing order
        odd_index_elements.sort(reverse=True)
        
        # Merge the sorted elements back into the original list
        result = []
        even_index = 0
        odd_index = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even_index_elements[even_index])
                even_index += 1
            else:
                result.append(odd_index_elements[odd_index])
                odd_index += 1
        
        return result

def sortEvenOdd(nums: List[int]) -> List[int]:
    return Solution().sortEvenOdd(nums)