import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # Create a set to store distinct integers
        distinct_integers = set(nums)
        
        # Function to reverse the digits of a number
        def reverse_number(n: int) -> int:
            return int(str(n)[::-1])
        
        # Add the reversed numbers to the set
        for num in nums:
            distinct_integers.add(reverse_number(num))
        
        # The size of the set is the number of distinct integers
        return len(distinct_integers)

def countDistinctIntegers(nums: List[int]) -> int:
    return Solution().countDistinctIntegers(nums)