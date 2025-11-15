import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Precompute the parity of each number in nums
        parity = [num % 2 for num in nums]
        
        # Function to check if a subarray is special
        def is_special(subarray):
            for i in range(len(subarray) - 1):
                if subarray[i] == subarray[i + 1]:
                    return False
            return True
        
        # Process each query
        result = []
        for start, end in queries:
            subarray_parity = parity[start:end + 1]
            result.append(is_special(subarray_parity))
        
        return result

def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[bool]:
    return Solution().isArraySpecial(nums, queries)