import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # Calculate the greatest common divisor (GCD) of all elements in numsDivide
        gcd_numDivide = reduce(gcd, numsDivide)
        
        # Sort nums to find the smallest element that divides gcd_numDivide
        nums.sort()
        
        # Iterate through nums to find the smallest element that divides gcd_numDivide
        for index, num in enumerate(nums):
            if gcd_numDivide % num == 0:
                return index
        
        # If no such element is found, return -1
        return -1

def minOperations(nums: List[int], numsDivide: List[int]) -> int:
    return Solution().minOperations(nums, numsDivide)