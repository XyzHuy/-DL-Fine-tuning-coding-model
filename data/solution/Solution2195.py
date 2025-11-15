import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        # Convert nums to a set to remove duplicates and allow O(1) lookups
        num_set = set(nums)
        # Initialize the smallest candidate number to be appended
        candidate = 1
        # This will store the sum of the k unique positive integers
        result_sum = 0
        
        # Iterate until we have found k unique numbers
        while k > 0:
            # If the candidate number is not in the set, it's a valid number to append
            if candidate not in num_set:
                result_sum += candidate
                k -= 1
            # Move to the next candidate number
            candidate += 1
        
        return result_sum

def minimalKSum(nums: List[int], k: int) -> int:
    return Solution().minimalKSum(nums, k)